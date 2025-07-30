"""
Configuration file for Employee Churn Prediction Application
"""

# Application Settings
APP_TITLE = "Employee Churn Prediction Dashboard"
APP_ICON = "👥"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Authentication
LOGIN_USERNAME = "admin"
LOGIN_PASSWORD = "password"

# Model Settings
MODEL_FILE = "logistic_regression_model.pkl"
SCALER_FILE = "scaler.pkl"
LABEL_ENCODERS_FILE = "label_encoders.pkl"
DATA_FILE = "HR_comma_sep.csv"

# UI Colors and Styling
COLORS = {
    "primary_gradient": "linear-gradient(90deg, #667eea 0%, #764ba2 100%)",
    "success_gradient": "linear-gradient(135deg, #11998e 0%, #38ef7d 100%)",
    "warning_gradient": "linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%)",
    "info_gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
    "sidebar_gradient": "linear-gradient(180deg, #667eea 0%, #764ba2 100%)"
}

# Prediction Thresholds
PREDICTION_THRESHOLDS = {
    "high_retention": 0.7,
    "moderate_risk": 0.5,
    "high_risk": 0.3
}

# Feature Ranges
FEATURE_RANGES = {
    "satisfaction_level": (0.0, 1.0, 0.5, 0.01),
    "last_evaluation": (0.0, 1.0, 0.5, 0.01),
    "number_project": (1, 10, 5, 1),
    "average_monthly_hours": (80, 400, 200, 10),
    "time_spend_company": (1, 10, 5, 1)
}

# Department Options
DEPARTMENTS = [
    'sales', 'accounting', 'hr', 'technical', 'support', 
    'management', 'IT', 'product_mng', 'marketing', 'RandD'
]

# Salary Options
SALARY_LEVELS = ['low', 'medium', 'high']

# Navigation Pages
NAVIGATION_PAGES = [
    "🏠 Dashboard",
    "🔮 Prediction", 
    "📊 Analytics",
    "📈 Insights"
]

# Chart Settings
CHART_CONFIG = {
    "color_continuous_scale": "RdYlGn_r",
    "correlation_scale": "RdBu",
    "histogram_bins": 30
} 