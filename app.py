import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Suppress deprecation warning
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# Load data
data = pd.read_csv('HR_comma_sep.csv')  # Update with your dataset filename

# Define features (X) and target (y)
X = data[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours',
          'time_spend_company', 'Work_accident', 'promotion_last_5years', 'Department', 'salary']]
y = data['left']

# Encode categorical variables
label_encoders = {}
for col in ['Department', 'salary']:
    label_encoders[col] = LabelEncoder()
    X.loc[:, col] = label_encoders[col].fit_transform(X.loc[:, col])

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

    satisfaction_level = st.slider('Satisfaction Level', 0.0, 1.0, 0.5)
    last_evaluation = st.slider('Last Evaluation', 0.0, 1.0, 0.5)
    number_project = st.slider('Number of Projects', 0, 10, 5)
    average_monthly_hours = st.slider('Average Monthly Hours', 0, 400, 200)
    time_spend_company = st.slider('Years at Company', 1, 10, 5)
    work_accident = st.selectbox('Work Accident', ['No', 'Yes'])
    promotion_last_5years = st.selectbox(
        'Promotion in Last 5 Years', ['No', 'Yes'])
    department = st.selectbox('Department', [
                              'sales', 'accounting', 'hr', 'technical', 'support', 'management', 'IT', 'product_mng', 'marketing', 'RandD'])
    salary = st.selectbox('Salary', ['low', 'medium', 'high'])

    # Convert selected values to DataFrame
    input_data = pd.DataFrame({
        'satisfaction_level': [satisfaction_level],
        'last_evaluation': [last_evaluation],
        'number_project': [number_project],
        'average_montly_hours': [average_monthly_hours],
        'time_spend_company': [time_spend_company],
        'Work_accident': [1 if work_accident == 'Yes' else 0],
        'promotion_last_5years': [1 if promotion_last_5years == 'Yes' else 0],
        'Department': [department],
        'salary': [salary]
    })

    # Make prediction
    if st.button('Predict'):
        # Preprocess input data
        for col in ['Department', 'salary']:
            input_data.loc[:, col] = label_encoders[col].transform(
                input_data.loc[:, col])
        scaled_input_data = scaler.transform(input_data)

        # Predict outcome probabilities
        proba = logistic_classifier.predict_proba(scaled_input_data)
        st.markdown(f'<h1 style="color:green;">Probability of employee staying: {np.round(proba[0][0], 2)}</h1>',
                    unsafe_allow_html=True)
        st.markdown(f'<h1 style="color:red;">Probability of employee leaving: {np.round(proba[0][1], 2)}</h1>',
                    unsafe_allow_html=True)

    # Sidebar to select columns
    st.sidebar.title('Select Columns')
    selected_columns = st.sidebar.multiselect('Select columns:', data.columns)

    # Dynamic univariate plot
    st.header('Univariate Plot')

    if selected_columns:
        for column in selected_columns:
            st.subheader(f'Univariate plot for {column}')
            if data[column].dtype == 'object':
                sns.countplot(data=data, x=column)
                plt.xticks(rotation=45)
                st.pyplot()
            else:
                sns.histplot(data=data, x=column, kde=True)
                st.pyplot()

    # Dynamic bivariate plot
    st.header('Bivariate Plot')

    if len(selected_columns) >= 2:
        selected_columns_pair = st.sidebar.multiselect(
            'Select columns for bivariate plot:', selected_columns)
    
        if selected_columns_pair:
            for pair in selected_columns_pair:
                st.subheader(f'Bivariate plot for {pair}')
                
                # Check the columns of your data
                print("Columns in the data:", data.columns)

                # Verify the data types of each column
                print("Data types of each column:", data.dtypes)

                # Check for missing values in the data
                print("Missing values in the data:", data.isnull().sum())

                # Check the content of the 'pair' variable
                print("Content of 'pair' variable:", pair)

                # Optionally: Display this in Streamlit as well
                st.write("Columns in the data:", data.columns)
                st.write("Data types of columns:", data.dtypes)
                st.write("Missing values in the data:", data.isnull().sum())
                st.write("Pair variable:", pair)

                # Bivariate scatter plot
                sns.scatterplot(data=data, x=pair[0], y=pair[1])
                plt.xticks(rotation=45)
                plt.yticks(rotation=45)
                st.pyplot()
    else:
        st.warning('Please select at least two columns for bivariate plot.')

    # HTML footer
    st.markdown("""
    <footer style='text-align: center; padding: 20px; background-color: #f1f1f1; margin-top: 20px;'>
        <p>&copy; 2024 Employee Churn Prediction. All rights reserved.</p>
    </footer>
    """, unsafe_allow_html=True)