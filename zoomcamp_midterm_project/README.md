# Sales Prediction Machine Learning Project

This project is aimed at building a machine learning model to predict sales based on the investment in various advertising channels, including TV, radio, and newspaper budgets. The project includes data preprocessing, exploratory data analysis (EDA), model training, and deployment on AWS Elastic Beanstalk.

## Dataset

The dataset used in this project is stored in the `data` directory. It includes the following variables:
- `tv_budget`: Investment in TV advertising.
- `radio_budget`: Investment in radio advertising.
- `newspaper_budget`: Investment in newspaper advertising.
- `sales`: The target variable representing sales revenue.

##   Notebook.ipynb

The project's main analysis and development are documented in the `notebook.ipynb` Jupyter Notebook. This notebook contains the following sections:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Training various machine learning models using different algorithms

## Train.py

The `train.py` script is used to train the machine learning model that produced the lowest Root Mean Squared Error (RMSE) on the validation dataset. The selected algorithm is XGBoost. The trained model is saved in a binary file called 'model_midterm_project.bin'

## Predict.py

The `predict.py` script uses the trained model to predict sales. We use Flask to create a web service.

## Predict_test.py

Predictions can be called from the `predict_test.py` script. we send a dictionary specifying the budget for each advertising channel and the response it prints are the estimated sales for the budget you specified.

## Other files Included

- `Pipfile` and `Pipfile.lock`: Define the Python dependencies for the project.
- `Dockerfile`: Contains the configuration for building a Docker container for this project.

## Deployment

This project is deployed on AWS Elastic Beanstalk, accessible as a web service. The 'predict_test.py' script is already configured to send a POST request to the AWS URL where the web service is deployed.

## Usage

You can run the project locally or utilize the web service hosted on AWS Elastic Beanstalk with the predict_test.py file.
