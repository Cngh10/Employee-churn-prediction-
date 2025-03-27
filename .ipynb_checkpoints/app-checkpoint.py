import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Suppress warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
warnings.filterwarnings("ignore")

# Load data
file_path = "/Users/chandanmahato/Downloads/HR_comma_sep.csv"
df = pd.read_csv(file_path)

# Rename columns (case-sensitive correction)
df = df.rename(columns={'satisfaction_level': 'satisfaction',
                        'last_evaluation': 'evaluation',
                        'number_project': 'projectCount',
                        'average_montly_hours': 'averageMonthlyHours',
                        'time_spend_company': 'yearsAtCompany',
                        'Work_accident': 'workAccident',
                        'promotion_last_5years': 'promotion',
                        'sales': 'Department',  # Ensure correct column name
                        'left': 'turnover'})

# Print column names to verify
print(df.columns)

# Define features (X) and target (y)
X = df[['satisfaction', 'evaluation', 'projectCount', 'averageMonthlyHours',
        'yearsAtCompany', 'workAccident', 'promotion', 'Department', 'salary']]
y = df['turnover']

# Encode categorical variables
label_encoders = {}
for col in ['Department', 'salary']:  # Ensure column names match
    label_encoders[col] = LabelEncoder()
    X.loc[:, col] = label_encoders[col].fit_transform(X[col])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression Classifier
logistic_classifier = LogisticRegression(random_state=42)
logistic_classifier.fit(X_train_scaled, y_train)

# Save model and preprocessing objects
joblib.dump(logistic_classifier, 'logistic_regression_model.pkl')

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Login function
def login(username, password):
    if username == 'admin' and password == 'password':  # Replace with your credentials
        st.session_state['logged_in'] = True
    else:
        st.error('Incorrect username or password')

# Login form
if not st.session_state['logged_in']:
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        login(username, password)
else:
    st.title('Employee Churn Prediction with Logistic Regression')
    st.image("Coverpage.png")

    # Website description
    st.markdown("""
    Welcome to the Employee Churn Prediction application! This tool uses a Logistic Regression model to predict the likelihood of an employee leaving the company.
    The prediction is based on various factors such as satisfaction level, last evaluation, number of projects, average monthly hours, years at the company, work accidents,
    promotions in the last 5 years, department, and salary. Adjust the sliders and select options to input your data, and click 'Predict' to see the results.
    """)

    satisfaction = st.slider('Satisfaction Level', 0.0, 1.0, 0.5)
    evaluation = st.slider('Last Evaluation', 0.0, 1.0, 0.5)
    projectCount = st.slider('Number of Projects', 0, 10, 5)
    averageMonthlyHours = st.slider('Average Monthly Hours', 0, 400, 200)
    yearsAtCompany = st.slider('Years at Company', 1, 10, 5)
    workAccident = st.selectbox('Work Accident', ['No', 'Yes'])
    promotion = st.selectbox('Promotion in Last 5 Years', ['No', 'Yes'])
    department = st.selectbox('Department', df['Department'].unique())  # Use unique values
    salary = st.selectbox('salary', df['salary'].unique())  # Use unique values

    # Convert selected values to DataFrame
    input_data = pd.DataFrame({
        'satisfaction': [satisfaction],
        'evaluation': [evaluation],
        'projectCount': [projectCount],
        'averageMonthlyHours': [averageMonthlyHours],
        'yearsAtCompany': [yearsAtCompany],
        'workAccident': [1 if workAccident == 'Yes' else 0],
        'promotion': [1 if promotion == 'Yes' else 0],
        'Department': [department],
        'salary': [salary]
    })

    # Make prediction
    if st.button('Predict'):
        # Preprocess input data
        for col in ['Department', 'salary']:
            input_data[col] = label_encoders[col].transform(input_data[col])
        scaled_input_data = scaler.transform(input_data)

        # Predict outcome probabilities
        proba = logistic_classifier.predict_proba(scaled_input_data)
        st.markdown(f'<h1 style="color:green;">Probability of employee staying: {np.round(proba[0][0], 2)}</h1>',
                    unsafe_allow_html=True)
        st.markdown(f'<h1 style="color:red;">Probability of employee leaving: {np.round(proba[0][1], 2)}</h1>',
                    unsafe_allow_html=True)

    # Sidebar to select columns
    st.sidebar.title('Select Columns')
    selected_columns = st.sidebar.multiselect('Select columns:', df.columns)

    # Dynamic univariate plot
    st.header('Univariate Plot')

    if selected_columns:
        for column in selected_columns:
            st.subheader(f'Univariate plot for {column}')
            fig, ax = plt.subplots()
            if df[column].dtype == 'object':
                sns.countplot(data=df, x=column, ax=ax)
                plt.xticks(rotation=45)
            else:
                sns.histplot(data=df, x=column, kde=True, ax=ax)
            st.pyplot(fig)

    # Dynamic bivariate plot
    st.header('Bivariate Plot')

    if len(selected_columns) >= 2:
    selected_columns_pair = st.sidebar.multiselect(
        'Select two columns for bivariate plot:', 
        df.columns, 
        default=selected_columns[:2] if len(selected_columns) >= 2 else None
    )

    if len(selected_columns_pair) == 2:  # Ensure exactly two columns are selected
        st.subheader(f'Bivariate plot for {selected_columns_pair[0]} vs {selected_columns_pair[1]}')
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=selected_columns_pair[0], y=selected_columns_pair[1], ax=ax)
        st.pyplot(fig)
    else:
        st.warning('Please select exactly two columns for the bivariate plot.')

    # HTML footer
    st.markdown("""
    <footer style='text-align: center; padding: 20px; background-color: #f1f1f1; margin-top: 20px;'>
        <p>&copy; 2024 Employee Churn Prediction. All rights reserved.</p>
    </footer>
    """, unsafe_allow_html=True)