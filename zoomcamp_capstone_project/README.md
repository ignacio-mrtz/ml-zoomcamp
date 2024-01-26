
# Predicting On-Time Delivery in International E-Commerce

## Problem Description: 

In this project, the primary objective is to develop a machine learning model capable of predicting whether products shipped by an international e-commerce company will be delivered on time. By predicting whether a shipment will be delivered on time, we aim to proactively address potential delays and improve the overall efficiency of the delivery system. . This problem arises from the critical need to enhance customer satisfaction and optimize the logistics and supply chain processes.

## Data:

To achieve this goal, we will train our model with the following dataset: [data/ecom-shipping](https://github.com/ignacio-mrtz/ml-zoomcamp/tree/main/zoomcamp_capstone_project/data)

Each row contains information about a sale(customer information, detailed product specifications, and logistics information)

The dataset contains 10999 observations of 12 variables:  

ID: ID Number of Customers.  
Warehouse block: The Company have big Warehouse which is divided in to block such as A,B,C,D,E.  
Mode of shipment:The Company Ships the products in multiple way such as Ship, Flight and Road.  
Customer care calls: The number of calls made from enquiry for enquiry of the shipment.  
Customer rating: The company has rated from every customer. 1 is the lowest (Worst), 5 is the highest (Best).  
Cost of the product: Cost of the Product in US Dollars.  
Prior purchases: The Number of Prior Purchase.  
Product importance: The company has categorized the product in the various parameter such as low, medium, high.  
Gender: Male and Female.  
Discount offered: Discount offered on that specific product.  
Weight in gms: It is the weight in grams.  
Reached on time: It is the target variable, where 1 Indicates that the product has NOT reached on time and 0 indicates it has reached on time.  

##   Notebook.ipynb

The project's main analysis and development are documented in the `notebook.ipynb` Jupyter Notebook. This notebook contains the following sections:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Training various machine learning models with different algorithms

## Train.py

The `train.py` script is used to train the machine learning model that produced the best accuracy on the validation dataset. The selected algorithm is XGBoost. The trained model is saved in a binary file called 'model_capstone_project.bin'

## Predict.py

The `predict.py` script uses the trained model to predict sales. We use Flask to create a web service.

## Predict-test.py

Predictions can be called from the `predict-test.py` script. we send a dictionary specifying details of the sale and the web service will predict if the product will arrive on time or not.

## Other files Included

- `Pipfile` and `Pipfile.lock`: Define the Python dependencies for the project.
- `Dockerfile`: Contains the configuration for building a Docker container for this project.

## Deployment

This project is deployed on AWS Elastic Beanstalk, accessible as a web service. The 'predict-test.py' script is already configured to send a POST request to the AWS URL where the web service is deployed.

## Usage

You can run the project locally or utilize the web service hosted on AWS Elastic Beanstalk with the predict_test.py file.

## Instructions on How to Run the Project

### To test the web service deployed on aws elastic beanstalk:  

On your terminal CD to the directory where you want to clone the project folder and then:

<pre>
git clone https://github.com/ignacio-mrtz/ml-zoomcamp
</pre>
<pre>
 cd ml-zoomcamp/
</pre>
<pre>
 cd zoomcamp_capstone_project/
</pre>
<pre>
python predict-test.py
 </pre>
 
if you could not run it check you have the requests library installed(if not "pip install requests").

you can play with different values in the python dict sent to the web service.  

### To build a docker container and test it locally:  

<pre>
git clone https://github.com/ignacio-mrtz/ml-zoomcamp
</pre>
<pre>
 cd ml-zoomcamp/
</pre>
<pre>
 cd zoomcamp_capstone_project/
</pre>
<pre>
docker build -t zoomcamp_capstone_project .
</pre>
<pre>
docker run -it --rm -p 9696:9696 zoomcamp_capstone_project
</pre>

and now modify the following lines of code in the predict-test.py file:
<pre>
url="http://localhost:9696/predict"
#host_for_aws="shipping-serving-env.eba-6ip2ev52.us-west-2.elasticbeanstalk.com."
#url_for_aws=f'http://{host_for_aws}/predict'

response=requests.post(url,json=sale_data).json()
</pre>

and last, from another terminal but on the same directory:  
<pre>
 python predict-test.py
</pre>






