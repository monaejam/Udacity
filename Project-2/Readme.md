
### Architectural Diagram

first we do authentication then we use our auto ml model then we deploy it then when enable the logging then we consume the model endpoint then we create a pipeline and document everything












Before starting our experiment, we first register the dataset and configure a compute cluster for training. Automated Machine Learning (AutoML) is used to find the best classification model. The best model is then deployed as an HTTP REST endpoint using Azure Container Instances with authentication enabled. Application Insights is enabled for the deployed model using the logs.py script. We interact with the deployed model's documentation using Swagger. Finally, the model is consumed using the endpoint.py script.

The dataset registered: 
 


The status of auto ml when completed  after 38 minutes
 



The best model is voting ensemble and AUC weghited is 0.97 

This is the endpoint after interaction with logs.py it become enabled 
 


This is the log from the GUI

 












This is the pipeline 
 
When it gets successful 
 
 This is when we interact with the endpoint using the primary key and and authentication key , the name of the job is aciservice the same as above . Also this is the graph












 



 







 





The result of interactions 



 


The trace of working with the model 



 
Also using swagger to interact with the model 

 


Future recommendation : 
•  Implement Deep Learning: This approach could potentially boost model performance. However, it would necessitate scaling up both the dataset and the compute resources to handle the increased complexity and ensure faster training times.
•  Mitigate Class Imbalance: The dataset is significantly imbalanced, which can cause the model to favor the majority class. Applying techniques to balance the data could lead to more accurate and fair predictions.


Video recording link

https://www.loom.com/share/d6d35b0aa9aa4d8ba222476d3b35cd41?sid=9ea7b62c-e879-4577-bd29-004ab36d688e

![image](https://github.com/user-attachments/assets/d52b5504-6414-4b87-82ca-d3b5d5fdffee)
