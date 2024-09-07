Before starting our experiment, we first register the dataset and configure a compute cluster for training. Automated Machine Learning (AutoML) is used to find the best classification model. The best model is then deployed as an HTTP REST endpoint using Azure Container Instances with authentication enabled. Application Insights is enabled for the deployed model using the logs.py script. We interact with the deployed model's documentation using Swagger. Finally, the model is consumed using the endpoint.py script.

<img width="530" alt="image" src="https://github.com/user-attachments/assets/bfa403cd-a390-418e-8dae-15bbd0537145">


automl.ipynb : It is the notebook file for the AutoML.
endpoint.py : This is the python script  used to consume the produced endpoint.
### Dataset being created :
<img width="540" alt="image" src="https://github.com/user-attachments/assets/e8e7970a-a525-4fa9-b976-284e1d916034">

The run created not active yet 

<img width="540" alt="image" src="https://github.com/user-attachments/assets/841597f3-712f-4bc4-b9d7-9c12a60daba4">

### The auto Ml run  is setting up  to be activated 
it is using our dataset created in previous step



<img width="540" alt="image" src="https://github.com/user-attachments/assets/7e5c0d7d-3b4b-4feb-9151-4348f9dd19fe">

### It is running now and the primary metric is AUC weighted 
Once completed, the status will change from running to complete


<img width="540" alt="image" src="https://github.com/user-attachments/assets/20e693ff-786e-4df5-af55-413b14e16926">



### It has been completed after   32 min These are what I used in the AutoMl notebook

    task='classification',
    primary_metric='accuracy',
    training_data=dataset,  
    label_column_name='y',
    compute_target=compute_target




<img width="540" alt="image" src="https://github.com/user-attachments/assets/20a6f52a-938f-4bd7-bbf2-291bb3883f94">


#### Voting Ensemble was found to be the best model with an accuracy of 0.9478


<img width="540" alt="image" src="https://github.com/user-attachments/assets/78de7886-0333-40b3-9c21-ca9519f09252">


### The image below shows few other metrics for the Best Model (Voting Ensemble) 
such as precision and F1 score

<img width="540" alt="image" src="https://github.com/user-attachments/assets/30bac166-0cac-4370-a077-a6f45bf521db">


### The pipeline is created and is running 

<img width="540" alt="image" src="https://github.com/user-attachments/assets/c0550cb8-2200-460e-9997-ae3cbe80c8f9">


### Here is the details of the run :

<img width="540" alt="image" src="https://github.com/user-attachments/assets/9ec9a8eb-dc88-44a0-9412-69a22c8fe7e6">


### After the completion status of pipeline changed to completion :
 pipeline is used to orchestrate and automate machine learning workflows. It allows us to define, schedule, and execute complex processes consisting of multiple steps, such as data preparation, training, evaluation, and deployment of machine learning models.




<img width="540" alt="image" src="https://github.com/user-attachments/assets/8d32a1fa-6187-4bcd-a97b-f33b8592245d">




### We did not enable application insights at model deployment, hence a status of False is shown!

it means  monitoring and telemetry service, is not actively collecting data for the resource.

<img width="540" alt="image" src="https://github.com/user-attachments/assets/3ed48d7c-e7dd-43f8-944c-2f01b6c5ee7d">


### Here is the trace of running logs.py in terminal and the application insight become true
which means we  can send custom telemetry or logging data to Application Insights or another service

<img width="540" alt="image" src="https://github.com/user-attachments/assets/fa3bc3b2-b2e2-45d1-bc5e-6bd47786a85d">




<img width="540" alt="image" src="https://github.com/user-attachments/assets/c4e8ac6e-adb9-43c6-9091-28d1d031cdf6">



### One more time  we can see the pipeline is created  and is active
Once an AutoML run has trained and identified the best model, deploying that model into a production environment can be automated and scaled using Azure ML pipelines. which we did in this step 

<img width="540" alt="image" src="https://github.com/user-attachments/assets/fbbb7b00-93ca-4d0d-a58d-281b327f4976">



### Finishing the pipeline in the endpoint shows that the job is completed 


<img width="540" alt="image" src="https://github.com/user-attachments/assets/bec24fe7-4ff5-43a5-91e8-56bef8be11d7">


<img width="540" alt="image" src="https://github.com/user-attachments/assets/e1389a29-f849-48d1-b964-fbfd3dbc5f43">



<img width="540" alt="image" src="https://github.com/user-attachments/assets/56dc2409-ed82-4686-a70a-f670de0bfc7b">



###  Run completed in above and details in following pic
Run Details Widget in the Jupyter Notebook provides details such as run logs, duration, steps etc.




<img width="540" alt="image" src="https://github.com/user-attachments/assets/c734bead-ebff-407e-a84c-59066ed21e1f">



### And finally the model is healthy and deployed !
The model was deployed to an ACI (Azure Container Instance)



<img width="540" alt="image" src="https://github.com/user-attachments/assets/27f6c99f-9faf-49d6-843e-bc380397aa66">


### And here is consuming the endpoint  we can see yes and no !
we can use terminal to interact with the model with the endpoint.py to test it 


<img width="540" alt="image" src="https://github.com/user-attachments/assets/6cd87ed9-2e4a-4dbf-9541-74973093b0bf">

<img width="540" alt="image" src="https://github.com/user-attachments/assets/776f4b4c-1e97-43c8-9c73-3ed1164b0bec">


### Also using swagger to interact with the model !
 Swagger is primarily used to generate interactive API documentation. 
This makes it easy for developers and API consumers to understand how to interact with the API.




<img width="540" alt="image" src="https://github.com/user-attachments/assets/abc4cc63-cc1b-491b-9e50-dd987bc917ef">



### Link to the video 


https://www.loom.com/share/5a9e1aa78c404662b8b74e6b55092716

### Future recommendation : 
•  Implement Deep Learning: This approach could potentially boost model performance. However, it would necessitate scaling up both the dataset and the compute resources to handle the increased complexity and ensure faster training times.
•  Mitigate Class Imbalance: The dataset is significantly imbalanced, which can cause the model to favor the majority class. Applying techniques to balance the data could lead to more accurate and fair predictions.


PIPEline
Add a CI/CD pipeline to interact with the Published Pipeline and trigger AutoML training run on scheduled or adhoc basis































































