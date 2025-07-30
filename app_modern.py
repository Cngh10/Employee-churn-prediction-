import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Employee Churn Prediction",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .warning-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .info-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSelectbox > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Load data and models
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('HR_comma_sep.csv')
        return data
    except:
        st.error("Error loading data file. Please ensure 'HR_comma_sep.csv' is in the current directory.")
        return None

@st.cache_resource
def load_models():
    try:
        model = joblib.load('logistic_regression_model.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoders = joblib.load('label_encoders.pkl')
        return model, scaler, label_encoders
    except:
        st.error("Error loading models. Please ensure model files are present.")
        return None, None, None

# Login function
def login(username, password):
    if username == 'admin' and password == 'password':
        st.session_state['logged_in'] = True
        st.success('Login successful!')
        st.rerun()
    else:
        st.error('Incorrect username or password')

# Main application
def main():
    # Login page
    if not st.session_state['logged_in']:
        st.markdown('<h1 class="main-header">🔐 Employee Churn Prediction</h1>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div class="info-card">
                <h3>Welcome to Employee Churn Prediction System</h3>
                <p>Please login to access the prediction dashboard</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                username = st.text_input("👤 Username")
                password = st.text_input("🔒 Password", type="password")
                submit_button = st.form_submit_button("🚀 Login")
                
                if submit_button:
                    login(username, password)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 3rem;">
            <p><strong>Demo Credentials:</strong></p>
            <p>Username: admin | Password: password</p>
        </div>
        """, unsafe_allow_html=True)
        
        return

    # Main dashboard
    st.markdown('<h1 class="main-header">👥 Employee Churn Prediction Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data and models
    data = load_data()
    model, scaler, label_encoders = load_models()
    
    if data is None or model is None:
        st.error("Failed to load data or models. Please check your files.")
        return

    # Sidebar
    st.sidebar.markdown("## 🎛️ Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Dashboard", "🔮 Prediction", "📊 Analytics", "📈 Insights"]
    )

    if page == "🏠 Dashboard":
        show_dashboard(data)
    elif page == "🔮 Prediction":
        show_prediction_page(data, model, scaler, label_encoders)
    elif page == "📊 Analytics":
        show_analytics_page(data)
    elif page == "📈 Insights":
        show_insights_page(data)

def show_dashboard(data):
    st.markdown("## 📊 Dashboard Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total Employees</h3>
            <h2>{len(data):,}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        churn_rate = (data['left'].sum() / len(data)) * 100
        st.markdown(f"""
        <div class="metric-card">
            <h3>Churn Rate</h3>
            <h2>{churn_rate:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_satisfaction = data['satisfaction_level'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Avg Satisfaction</h3>
            <h2>{avg_satisfaction:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_evaluation = data['last_evaluation'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h3>Avg Evaluation</h3>
            <h2>{avg_evaluation:.2f}</h2>
        </div>
        """, unsafe_allow_html=True)

    # Quick charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Churn Distribution")
        fig = px.pie(data, names='left', title='Employee Churn Status')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Satisfaction vs Churn")
        fig = px.box(data, x='left', y='satisfaction_level', 
                    title='Satisfaction Level by Churn Status')
        st.plotly_chart(fig, use_container_width=True)

def show_prediction_page(data, model, scaler, label_encoders):
    st.markdown("## 🔮 Employee Churn Prediction")
    
    st.markdown("""
    <div class="info-card">
        <h3>How to use:</h3>
        <p>Adjust the parameters below to predict the likelihood of an employee leaving the company. 
        The model considers various factors including satisfaction level, performance metrics, and organizational factors.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Employee Metrics")
        satisfaction_level = st.slider('Satisfaction Level', 0.0, 1.0, 0.5, 0.01)
        last_evaluation = st.slider('Last Evaluation Score', 0.0, 1.0, 0.5, 0.01)
        number_project = st.slider('Number of Projects', 1, 10, 5)
        average_monthly_hours = st.slider('Average Monthly Hours', 80, 400, 200)
        
    with col2:
        st.subheader("🏢 Organizational Factors")
        time_spend_company = st.slider('Years at Company', 1, 10, 5)
        work_accident = st.selectbox('Work Accident', ['No', 'Yes'])
        promotion_last_5years = st.selectbox('Promotion in Last 5 Years', ['No', 'Yes'])
        department = st.selectbox('Department', [
            'sales', 'accounting', 'hr', 'technical', 'support', 
            'management', 'IT', 'product_mng', 'marketing', 'RandD'
        ])
        salary = st.selectbox('Salary Level', ['low', 'medium', 'high'])
    
    # Prediction button
    if st.button('🔮 Predict Churn Probability', use_container_width=True):
        # Prepare input data with correct column names (matching the trained model)
        input_data = pd.DataFrame({
            'satisfaction': [satisfaction_level],
            'evaluation': [last_evaluation],
            'projectCount': [number_project],
            'averageMonthlyHours': [average_monthly_hours],
            'yearsAtCompany': [time_spend_company],
            'workAccident': [1 if work_accident == 'Yes' else 0],
            'promotion': [1 if promotion_last_5years == 'Yes' else 0],
            'Department': [department],
            'salary': [salary]
        })
        
        # Preprocess input data
        for col in ['Department', 'salary']:
            input_data.loc[:, col] = label_encoders[col].transform(input_data.loc[:, col])
        
        scaled_input_data = scaler.transform(input_data)
        
        # Make prediction
        proba = model.predict_proba(scaled_input_data)
        stay_prob = proba[0][0]
        leave_prob = proba[0][1]
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            if stay_prob > 0.7:
                st.markdown(f"""
                <div class="prediction-card">
                    <h2>🎉 High Retention Probability</h2>
                    <h1>{stay_prob:.1%}</h1>
                    <p>This employee is likely to stay with the company.</p>
                </div>
                """, unsafe_allow_html=True)
            elif stay_prob > 0.5:
                st.markdown(f"""
                <div class="prediction-card">
                    <h2>⚠️ Moderate Retention Risk</h2>
                    <h1>{stay_prob:.1%}</h1>
                    <p>Consider retention strategies for this employee.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="warning-card">
                    <h2>🚨 High Churn Risk</h2>
                    <h1>{leave_prob:.1%}</h1>
                    <p>Immediate attention required for retention.</p>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Probability chart
            fig = go.Figure(data=[
                go.Bar(x=['Stay', 'Leave'], y=[stay_prob, leave_prob],
                      marker_color=['#38ef7d', '#ff6b6b'])
            ])
            fig.update_layout(
                title="Prediction Probabilities",
                yaxis_title="Probability",
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

def show_analytics_page(data):
    st.markdown("## 📊 Data Analytics")
    
    # Feature analysis
    st.subheader("🔍 Feature Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Satisfaction distribution
        fig = px.histogram(data, x='satisfaction_level', color='left',
                          title='Satisfaction Level Distribution by Churn Status',
                          nbins=30)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Evaluation vs Satisfaction
        fig = px.scatter(data, x='satisfaction_level', y='last_evaluation', 
                        color='left', title='Satisfaction vs Evaluation')
        st.plotly_chart(fig, use_container_width=True)
    
    # Department analysis
    st.subheader("🏢 Department Analysis")
    dept_churn = data.groupby('Department')['left'].agg(['count', 'sum', 'mean']).reset_index()
    dept_churn.columns = ['Department', 'Total_Employees', 'Churned_Employees', 'Churn_Rate']
    
    fig = px.bar(dept_churn, x='Department', y='Churn_Rate',
                 title='Churn Rate by Department',
                 color='Churn_Rate',
                 color_continuous_scale='RdYlGn_r')
    st.plotly_chart(fig, use_container_width=True)
    
    # Salary analysis
    st.subheader("💰 Salary Analysis")
    salary_churn = data.groupby('salary')['left'].agg(['count', 'sum', 'mean']).reset_index()
    salary_churn.columns = ['Salary', 'Total_Employees', 'Churned_Employees', 'Churn_Rate']
    
    fig = px.bar(salary_churn, x='Salary', y='Churn_Rate',
                 title='Churn Rate by Salary Level',
                 color='Churn_Rate',
                 color_continuous_scale='RdYlGn_r')
    st.plotly_chart(fig, use_container_width=True)

def show_insights_page(data):
    st.markdown("## 📈 Key Insights")
    
    # Correlation analysis
    st.subheader("🔗 Feature Correlations")
    
    # Create correlation matrix
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    corr_matrix = data[numeric_cols].corr()
    
    fig = px.imshow(corr_matrix, 
                    title='Feature Correlation Matrix',
                    color_continuous_scale='RdBu',
                    aspect='auto')
    st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    st.subheader("💡 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🎯 Top Churn Factors</h3>
            <ul>
                <li>Low satisfaction level</li>
                <li>High evaluation with low satisfaction</li>
                <li>Long working hours</li>
                <li>No promotions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>📊 Retention Strategies</h3>
            <ul>
                <li>Improve work-life balance</li>
                <li>Provide career growth opportunities</li>
                <li>Regular feedback and recognition</li>
                <li>Competitive compensation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Time series analysis
    st.subheader("⏰ Time-based Patterns")
    
    # Years at company vs churn
    fig = px.box(data, x='time_spend_company', y='satisfaction_level', 
                color='left', title='Satisfaction by Years at Company')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main() 