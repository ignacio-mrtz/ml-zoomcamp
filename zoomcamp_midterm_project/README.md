# Sales Prediction Machine Learning Project

This project is aimed at building a machine learning model to predict sales based on the investment in various advertising channels, including TV, radio, and newspaper budgets. The project includes data preprocessing, exploratory data analysis (EDA), model training, and deployment on AWS Elastic Beanstalk.

## Dataset

The dataset used in this project is stored in the `data` directory. It includes the following variables:
- `tv_budget`: Investment in TV advertising.
- `radio_budget`: Investment in radio advertising.
- `newspaper_budget`: Investment in newspaper advertising.
- `sales`: The target variable representing sales revenue.

## Jupyter Notebook

The project's main analysis and development are documented in the `notebook.ipynb` Jupyter Notebook. This notebook contains the following sections:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Training various machine learning models using different algorithms

## Model Training

The `train.py` script is used to train the machine learning model that produced the lowest Root Mean Squared Error (RMSE) on the validation dataset. The selected algorithm is XGBoost with parameter tuning. The trained model is saved in a binary file.

## Prediction

The `predict.py` script uses the trained model to predict sales based on a dictionary specifying the budget for each advertising channel. Predictions can be called from the `predict_test.py` script.

## Deployment

This project is deployed on AWS Elastic Beanstalk, making it accessible as a web service.

## Files Included

- `Dockerfile`: Contains the configuration for building a Docker container for this project.
- `Pipfile` and `Pipfile.lock`: Define the Python dependencies for the project.

## Usage

You can run the project locally or utilize the web service hosted on AWS Elastic Beanstalk with the predict_test.py file.
