# Fast API Project
This project demonstrates a FastAPI application deployed on AWS. The app is containerized using Docker and configured for deployment with Amazon Web Services (AWS) services.

## Features
- FastAPI -  High-performance web framework for building APIs.
- Docker - Containerize the application for easy deployment.
- AWS Deployment - Deploy the app to AWS AWS Lambda with API Gateway.
- Environment Variables - Manage configuration with a .env file.

## Prerequisites
- AWS Account - Set up an AWS account.
- AWS CLI - Install the AWS CLI and configure it with aws configure.
- Docker - Install Docker to build and run containers.
- Python - Install Python (3.8+) for the FastAPI app.

## Setup
### 1. Create virtual environment and install depencies
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# upgrade
pip freeze > requirements.txt
```

### 2. Define environment variables
```sh
# touch .env
SECRET_KEY="your-secret-key"
DATABASE_URL="your-database-url"
```

### 3. Run application locally
```sh
uvicorn app.main:app --reload
```

