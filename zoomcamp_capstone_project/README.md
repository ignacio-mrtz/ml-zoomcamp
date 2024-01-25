
Predicting On-Time Delivery in International E-Commerce

Problem Description: 

In this project, the primary objective is to develop a machine learning model capable of predicting whether products shipped by an international e-commerce company will be delivered on time. By predicting whether a shipment will be delivered on time, we aim to proactively address potential delays and improve the overall efficiency of the delivery system. . This problem arises from the critical need to enhance customer satisfaction and optimize the logistics and supply chain processes.

Data:

To achieve this goal, we will train our model with the following dataset: [data/ecom-shipping](https://github.com/ignacio-mrtz/ml-zoomcamp/tree/main/zoomcamp_capstone_project/data)

Each row of the dataset contains information about a sale(customer information, detailed product specifications, and logistics information)

Content:

The dataset used for model building contains 10999 observations of 12 variables.
The data contains the following information:

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


Instructions on How to Run the Project:



