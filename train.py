import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
file_path = "/Users/chandanmahato/Downloads/HR_comma_sep.csv"  # Ensure the correct file path
df = pd.read_csv(file_path)

# Rename columns (to match app.py)
df = df.rename(columns={'satisfaction_level': 'satisfaction',
                        'last_evaluation': 'evaluation',
                        'number_project': 'projectCount',
                        'average_montly_hours': 'averageMonthlyHours',
                        'time_spend_company': 'yearsAtCompany',
                        'Work_accident': 'workAccident',
                        'promotion_last_5years': 'promotion',
                        'sales': 'Department',
                        'left': 'turnover'})

# Define features (X) and target (y)
X = df[['satisfaction', 'evaluation', 'projectCount', 'averageMonthlyHours',
        'yearsAtCompany', 'workAccident', 'promotion', 'Department', 'salary']]
y = df['left']

# Encode categorical variables
label_encoders = {}
for col in ['Department', 'salary']:
    label_encoders[col] = LabelEncoder()
    X[col] = label_encoders[col].fit_transform(X[col].copy())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression Classifier
logistic_classifier = LogisticRegression(random_state=42)
logistic_classifier.fit(X_train_scaled, y_train)

# Save model and preprocessing objects
# Load the model in the original environment (where it was trained)
model = joblib.load("logistic_regression_model.pkl")
# Re-save it using scikit-learn 1.1.3
joblib.dump(model, "logistic_regression_model_compatible.pkl")
joblib.dump(logistic_classifier, 'logistic_regression_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("Model and preprocessors saved successfully!")