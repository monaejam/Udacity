
### Architectural Diagram

first we do authentication then we use our auto ml model then we deploy it then when enable the logging then we consume the model endpoint then we create a pipeline and document everything


  <![image](https://github.com/user-attachments/assets/d52b5504-6414-4b87-82ca-d3b5d5fdffee)>


Before starting our experiment, we first register the dataset and configure a compute cluster for training. Automated Machine Learning (AutoML) is used to find the best classification model. The best model is then deployed as an HTTP REST endpoint using Azure Container Instances with authentication enabled. Application Insights is enabled for the deployed model using the logs.py script. We interact with the deployed model's documentation using Swagger. Finally, the model is consumed using the endpoint.py script.

### The dataset registered: 


  <img width="540" alt="image" src="https://github.com/user-attachments/assets/e1652c20-6fa6-4a1f-895f-dd1a1ec17b1b">



### The status of auto ml when completed  after 38 minutes


  
  <img width="540" alt="image" src="https://github.com/user-attachments/assets/0507c186-d1b7-45ff-94d3-f8818a7cd574">



### The best model is voting ensemble and AUC weghited is 0.97 

  <img width="540" alt="image" src="https://github.com/user-attachments/assets/60dbbb4f-4f91-41f4-921f-07036d3221b5">


### This is the endpoint after interaction with logs.py it become enabled 


 <img width="540" alt="image" src="https://github.com/user-attachments/assets/fa3230e7-1ffa-41eb-a694-f9e587ec75cc">



### This is the log from the GUI


   <img width="540" alt="image" src="https://github.com/user-attachments/assets/3e0fd6bb-3754-45cd-a0e6-78c67f7815c0">


 



### This is the pipeline


  <img width="540" alt="image" src="https://github.com/user-attachments/assets/e21c0498-13cd-4b2c-80d7-f37357f853a2">

 
### When it gets successful 


  <img width="540" alt="image" src="https://github.com/user-attachments/assets/d2e355e5-66d2-4eb4-bc36-937fe7a43c91">

 
 ### This is when we interact with the endpoint using the primary key and and authentication key , the name of the job is aciservice the same as above . Also this is the graph
 
   <img width="540" alt="image" src="https://github.com/user-attachments/assets/80b2021b-b6b2-44c8-bb65-ef94df5ca482">

                           
                           
  <img width="540" alt="image" src="https://github.com/user-attachments/assets/3ef7d4d9-f004-4031-8007-f7cac67b331f">


                          
                          
   <img width="540" alt="image" src="https://github.com/user-attachments/assets/d3f35403-0955-4b7f-9b21-6965f212c1c7">



### The result of interactions 



                              <img width="540" alt="image" src="https://github.com/user-attachments/assets/7e4165fc-9dbb-4827-8b69-4da1527431bf">



### The trace of working with the model 

                             <img width="540" alt="image" src="https://github.com/user-attachments/assets/f1dd21e8-f9a2-44c2-b684-74dfc5736899">


 
### Also using swagger to interact with the model 

                            <img width="540" alt="image" src="https://github.com/user-attachments/assets/29214f33-1186-4b04-a4de-714996883b9a">



### Future recommendation : 
•  Implement Deep Learning: This approach could potentially boost model performance. However, it would necessitate scaling up both the dataset and the compute resources to handle the increased complexity and ensure faster training times.
•  Mitigate Class Imbalance: The dataset is significantly imbalanced, which can cause the model to favor the majority class. Applying techniques to balance the data could lead to more accurate and fair predictions.


### Video recording link

https://www.loom.com/share/d6d35b0aa9aa4d8ba222476d3b35cd41?sid=9ea7b62c-e879-4577-bd29-004ab36d688e


