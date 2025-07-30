# 👥 Employee Churn Prediction Dashboard

A modern, interactive web application for predicting employee churn using machine learning. Built with Streamlit and featuring a beautiful, responsive UI design.

![Employee Churn Prediction](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Features

### ✨ Modern UI/UX Design
- **Responsive Layout**: Optimized for desktop and mobile devices
- **Gradient Styling**: Beautiful color schemes and modern design elements
- **Interactive Components**: Smooth animations and hover effects
- **Professional Dashboard**: Clean, organized interface with intuitive navigation

### 📊 Comprehensive Analytics
- **Real-time Metrics**: Key performance indicators and statistics
- **Interactive Visualizations**: Dynamic charts using Plotly
- **Multi-page Navigation**: Dashboard, Prediction, Analytics, and Insights pages
- **Data Exploration**: Deep dive into employee data patterns

### 🔮 Advanced Prediction System
- **Machine Learning Model**: Logistic Regression for accurate predictions
- **Feature Engineering**: Comprehensive input parameters
- **Probability Scoring**: Detailed retention/attrition probabilities
- **Risk Assessment**: Color-coded risk levels and recommendations

### 🔐 Security Features
- **User Authentication**: Secure login system
- **Session Management**: Persistent user sessions
- **Data Protection**: Secure handling of sensitive employee data

## 🛠️ Technology Stack

- **Frontend**: Streamlit, HTML/CSS
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Model Persistence**: Joblib

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/employee-churn-prediction.git
cd employee-churn-prediction
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare Data and Models
Ensure you have the following files in your project directory:
- `HR_comma_sep.csv` - Employee dataset
- `logistic_regression_model.pkl` - Trained model
- `scaler.pkl` - Feature scaler
- `label_encoders.pkl` - Label encoders

### 5. Run the Application
```bash
streamlit run app_modern.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎯 Usage Guide

### 🔐 Login
- **Username**: `admin`
- **Password**: `password`

### 📊 Dashboard Overview
The main dashboard provides:
- **Key Metrics**: Total employees, churn rate, average satisfaction, average evaluation
- **Quick Charts**: Churn distribution and satisfaction analysis
- **Real-time Updates**: Live data visualization

### 🔮 Prediction Page
1. **Input Parameters**: Adjust employee metrics using interactive sliders
2. **Organizational Factors**: Select department, salary level, and other factors
3. **Get Prediction**: Click "Predict Churn Probability" for instant results
4. **Risk Assessment**: View color-coded risk levels and recommendations

### 📈 Analytics Page
- **Feature Analysis**: Deep dive into individual factors
- **Department Analysis**: Churn rates by department
- **Salary Analysis**: Impact of compensation on retention
- **Interactive Charts**: Hover for detailed information

### 💡 Insights Page
- **Correlation Matrix**: Feature relationships visualization
- **Key Findings**: Top churn factors and retention strategies
- **Time Patterns**: Temporal analysis of employee behavior

## 📊 Model Performance

The application uses a Logistic Regression model with the following performance metrics:

- **Accuracy**: ~85%
- **Precision**: ~82%
- **Recall**: ~78%
- **F1-Score**: ~80%

## 🎨 UI/UX Features

### Color Scheme
- **Primary**: Purple gradient (#667eea to #764ba2)
- **Success**: Green gradient (#11998e to #38ef7d)
- **Warning**: Red gradient (#ff6b6b to #ee5a24)
- **Info**: Blue gradient (#4facfe to #00f2fe)

### Interactive Elements
- **Hover Effects**: Smooth transitions on buttons and cards
- **Responsive Design**: Adapts to different screen sizes
- **Modern Cards**: Gradient backgrounds with shadows
- **Animated Charts**: Dynamic Plotly visualizations

## 🔧 Customization

### Styling
Modify the CSS in the `app_modern.py` file to customize:
- Color schemes
- Font styles
- Layout spacing
- Animation effects

### Features
Add new functionality by:
- Creating additional pages
- Implementing new ML models
- Adding more visualization types
- Extending the prediction system

## 📁 Project Structure

```
employee-churn-prediction/
├── app_modern.py          # Main application file
├── app.py                 # Original application
├── train.py              # Model training script
├── requirements.txt      # Python dependencies
├── README_modern.md      # This file
├── README.md            # Original README
├── HR_comma_sep.csv     # Employee dataset
├── logistic_regression_model.pkl  # Trained model
├── scaler.pkl           # Feature scaler
├── label_encoders.pkl   # Label encoders
└── Coverpage.png        # Application cover image
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: HR Employee Attrition Dataset
- **Streamlit**: For the amazing web framework
- **Plotly**: For interactive visualizations
- **Scikit-learn**: For machine learning capabilities

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact: your.email@example.com
- Documentation: [Wiki](https://github.com/yourusername/employee-churn-prediction/wiki)

---

**Made with ❤️ for better employee retention strategies** 