# Deployment Guide

This guide provides instructions for deploying the Employee Churn Prediction application to various platforms.

## Local Development

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Quick Start
```bash
# Clone the repository
git clone https://github.com/Cngh10/Employee-churn-prediction-.git
cd Employee-churn-prediction-

# Run the application
./run_app.sh
```

## Streamlit Cloud Deployment

### Steps
1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your forked repository
6. Set the main file path to: `app_modern.py`
7. Click "Deploy"

### Configuration
- **Repository**: Your forked repository
- **Branch**: main
- **Main file path**: app_modern.py
- **Python version**: 3.8

## Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Heroku account

### Steps
1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create your-app-name`
4. Add buildpacks:
   ```bash
   heroku buildpacks:add heroku/python
   ```
5. Deploy: `git push heroku main`
6. Open the app: `heroku open`

### Required Files
- `requirements.txt` (already included)
- `Procfile` (create with content: `web: streamlit run app_modern.py --server.port=$PORT --server.address=0.0.0.0`)

## Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app_modern.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run
```bash
# Build the image
docker build -t employee-churn-app .

# Run the container
docker run -p 8501:8501 employee-churn-app
```

## Environment Variables

### Optional Configuration
- `STREAMLIT_SERVER_PORT`: Port number (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)
- `STREAMLIT_SERVER_HEADLESS`: Run in headless mode (default: true)

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find and kill the process
   lsof -ti:8501 | xargs kill -9
   ```

2. **Missing dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Model files not found**
   - Ensure all .pkl files are in the project directory
   - Check file permissions

4. **Data file not found**
   - Ensure HR_comma_sep.csv is in the project directory

### Performance Optimization

1. **Enable caching**
   - The app already uses Streamlit's caching decorators
   - Consider using Redis for production caching

2. **Load balancing**
   - Use multiple instances behind a load balancer
   - Configure proper session management

3. **Database optimization**
   - Consider using a database for large datasets
   - Implement proper indexing

## Security Considerations

1. **Authentication**
   - Change default login credentials in production
   - Implement proper user management
   - Use environment variables for sensitive data

2. **Data protection**
   - Ensure data is encrypted in transit
   - Implement proper access controls
   - Regular security audits

3. **API security**
   - Rate limiting
   - Input validation
   - CORS configuration

## Monitoring and Logging

### Streamlit Cloud
- Built-in monitoring and analytics
- Error tracking and performance metrics

### Custom Monitoring
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add logging to your app
logger.info("Application started")
```

## Backup and Recovery

1. **Data backup**
   - Regular backups of model files
   - Version control for configuration
   - Database backups if applicable

2. **Disaster recovery**
   - Document recovery procedures
   - Test backup restoration
   - Maintain multiple deployment environments

## Support

For deployment issues:
1. Check the troubleshooting section
2. Review Streamlit documentation
3. Create an issue in the GitHub repository
4. Contact the development team 