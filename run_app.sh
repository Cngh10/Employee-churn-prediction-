#!/bin/bash

echo "🚀 Starting Employee Churn Prediction Dashboard..."
echo "📦 Installing dependencies..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📦 Installing requirements..."
pip install -r requirements.txt

# Run the application
echo "🌟 Starting Streamlit application..."
echo "🌐 The app will open at: http://localhost:8501"
echo "🔐 Login credentials: admin / password"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app_modern.py 