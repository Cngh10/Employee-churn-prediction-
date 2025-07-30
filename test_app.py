"""
Test script for Employee Churn Prediction Application
"""

import pandas as pd
import joblib
import numpy as np
from config import *

def test_data_loading():
    """Test if data file can be loaded"""
    try:
        data = pd.read_csv(DATA_FILE)
        print(f"✅ Data loaded successfully: {len(data)} rows, {len(data.columns)} columns")
        return True
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return False

def test_model_loading():
    """Test if model files can be loaded"""
    try:
        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        label_encoders = joblib.load(LABEL_ENCODERS_FILE)
        print("✅ All model files loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Error loading models: {e}")
        return False

def test_prediction():
    """Test if prediction works with sample data"""
    try:
        # Load model and data
        model = joblib.load(MODEL_FILE)
        scaler = joblib.load(SCALER_FILE)
        label_encoders = joblib.load(LABEL_ENCODERS_FILE)
        data = pd.read_csv(DATA_FILE)
        
        # Create sample input with correct column names
        sample_input = pd.DataFrame({
            'satisfaction': [0.5],
            'evaluation': [0.6],
            'projectCount': [5],
            'averageMonthlyHours': [200],
            'yearsAtCompany': [3],
            'workAccident': [0],
            'promotion': [0],
            'Department': ['sales'],
            'salary': ['medium']
        })
        
        # Preprocess
        for col in ['Department', 'salary']:
            sample_input.loc[:, col] = label_encoders[col].transform(sample_input.loc[:, col])
        
        scaled_input = scaler.transform(sample_input)
        
        # Predict
        proba = model.predict_proba(scaled_input)
        print(f"✅ Prediction successful: Stay={proba[0][0]:.3f}, Leave={proba[0][1]:.3f}")
        return True
    except Exception as e:
        print(f"❌ Error in prediction: {e}")
        return False

def test_config():
    """Test configuration file"""
    try:
        print(f"✅ App title: {APP_TITLE}")
        print(f"✅ Departments: {len(DEPARTMENTS)} options")
        print(f"✅ Salary levels: {len(SALARY_LEVELS)} options")
        print(f"✅ Navigation pages: {len(NAVIGATION_PAGES)} pages")
        return True
    except Exception as e:
        print(f"❌ Error in config: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Employee Churn Prediction Application")
    print("=" * 50)
    
    tests = [
        ("Configuration", test_config),
        ("Data Loading", test_data_loading),
        ("Model Loading", test_model_loading),
        ("Prediction", test_prediction)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        if test_func():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Application is ready to run.")
        print("🚀 Run 'streamlit run app_modern.py' to start the application")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main() 