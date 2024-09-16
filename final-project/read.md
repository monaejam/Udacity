## overview of the project
This capstone project for the "Machine Learning Engineer for Microsoft Azure" Udacity Nanodegree involves selecting a public external dataset to train a model using two approaches: Automated Machine Learning (AutoML) and Hyperdrive. After comparing the performance of these methods, the best model will be deployed. The deployed model's endpoint will then be used to make predictions and answer relevant queries.


automl.ipynb: Notebook file used for running the AutoML experiments.
endpoint.py: Python script used to consume the deployed model's endpoint.
train.py: Python script utilized by Hyperdrive to perform runs and identify the best model.
hyperparameter_tuning.ipynb: Notebook used for running Hyperdrive experiments.
heart_failure_clinical_records_dataset.csv: Dataset used for the experiments.
env.yml: Environment file downloaded from Azure ML Studio.
hyper-model.pkl: The best model from Hyperdrive, downloaded from Azure ML Studio.
model.pkl: The best model from AutoML, downloaded from Azure ML Studio.
scoring_file_pbi_v_1_0_0.py: Script downloaded from Azure ML Studio for deploying the model.

 ## An overview of the dataset used
The dataset used, heart_failure_clinical_records_dataset.csv, contains recorded health indicators for nearly 300 patients. These metrics were collected to help predict the occurrence of the DEATH_EVENT, which indicates whether or not the patient passed away during the follow-up period (boolean).
The objective is to predict the DEATH_EVENT (whether the patient died during the follow-up period) using the following features:

age: The patient's age.
anaemia: Presence of decreased red blood cells or hemoglobin (boolean).
creatinine_phosphokinase: Level of the creatine phosphokinase enzyme (mcg/L).
diabetes: Whether the patient has diabetes (boolean).
ejection_fraction: Percentage of blood leaving the heart with each contraction (percentage).
high_blood_pressure: Whether the patient has hypertension (boolean).
platelets: Platelet count in the blood (kiloplatelets/mL).
serum_creatinine: Serum creatinine level in the blood (mg/dL).
serum_sodium: Serum sodium level in the blood (mEq/L).
sex: Gender of the patient (binary).
smoking: Smoking status (boolean).
time: Length of the follow-up period (days).
DEATH_EVENT: Whether the patient died during the follow-up period (boolean).


## An overview of the method used to get the data into your Azure ML Studio workspace.
GitHub Token and URL: A GitHub token and the dataset URL are defined to access the CSV file.

Fetching the Data: The script sends a request to GitHub to retrieve the dataset. If successful, the raw CSV content is read into a Pandas DataFrame.

Connecting to Azure ML: The workspace is accessed using Azure ML's Workspace.from_config() method.

Dataset Registration: The dataset is registered in Azure ML's default datastore as a Tabular dataset with the name "heart_failure_dataset."

Data Exploration: Once registered, the dataset is converted back to a Pandas DataFrame, and a descriptive summary is generated using describe().

<img width="540" alt="image" src="https://github.com/user-attachments/assets/0003ee6a-2e0f-4f91-a85a-75a571d02903">



## An overview of your AutoML experiment settings and configuration in your own words (please do not copy-paste the configuration from your code, try to explain instead)
In my AutoML experiment, I focused on configuring a classification task to predict whether or not a patient would experience the DEATH_EVENT. Here's an overview of the main settings:

Dataset: The heart failure dataset was sourced from a public URL, and I ensured it was either already registered or newly registered in the Azure ML Workspace.

Cross-Validation: I used 3-fold cross-validation to assess model performance, ensuring a reliable evaluation of models through repeated sampling.

Primary Metric: I chose AUC_weighted as the primary metric. This is useful for evaluating model performance on imbalanced datasets like this one, where the prediction of both classes (death/no death) is important.

Concurrency & Timeout: I set the experiment to run up to 6 models concurrently, optimizing the use of time and resources. Additionally, I capped the total run time to 30 minutes, ensuring that the experiment remains time-efficient.

Early Stopping & Ensembling: Early stopping was enabled to halt underperforming models quickly. Ensembling and stack ensembling were also activated to potentially improve the overall performance by combining the predictions of multiple models.

Blocked Models: XGBoost was specifically excluded from the model candidates, perhaps due to prior experience or specific requirements of the project.

Featurization: The featurization was set to auto, allowing AutoML to automatically handle the preprocessing and transformation of the features.

Output: All output was directed to a specific project folder, with logs saved in an error log file for easier debugging.

In summary, the AutoML configuration was designed to efficiently explore multiple models, focusing on performance, model diversity, and time management, while leveraging ensembling for improved accuracy.


## An overview of the types of parameters and their ranges used for the hyperparameter search
<img width="540" alt="image" src="https://github.com/user-attachments/assets/e2a05199-30f9-40f4-b409-60c1b6fb42fb">

In the hyperparameter search setup, several types of parameters and their ranges were defined, as well as a sampling strategy and early stopping policy to optimize model performance. Here's an overview:

1. **Parameter Sampling**: 
   - **`--C`**: This parameter, commonly associated with regularization strength, was tested with values ranging from 1 to 5.
   - **`--max_iter`**: This parameter controls the number of iterations for the model training, and values were sampled from 80, 100, 120, 150, 170, and 200.
   
   The **`RandomParameterSampling`** strategy was used to randomly select values from these ranges during the hyperparameter search.

2. **Early Stopping Policy**:
   - The **Bandit Policy** was used to terminate underperforming runs early. It monitored the model's performance at each evaluation interval (set to 1) and would stop any runs that performed significantly worse than the best model by a factor of 0.2 (20% worse).
   - The policy also delayed the evaluation of early runs for the first 5 iterations to ensure that the model had enough time to improve before being evaluated.

3. **HyperDrive Configuration**:
   - The **primary metric** for optimization was accuracy, and the goal was to maximize it.
   - The search allowed a maximum of 2 concurrent runs at a time, with a total of 10 runs to explore different hyperparameter combinations.
   
In summary, this setup aimed to efficiently explore the hyperparameter space by balancing exploration (random sampling) and exploitation (early stopping with the Bandit policy) to find the best model configuration.


## An overview of the two models with the best parameters

voting ensemble with the accuracy of 0.90759 comes as best from auto ml

<img width="540" alt="image" src="https://github.com/user-attachments/assets/ddbe454d-f756-4f8b-b101-0148e2e1bad3">

the hyper drive took 8 minutes and 35 seconds get to completed 
<img width="540" alt="image" src="https://github.com/user-attachments/assets/fcb09d40-818c-4e4c-bde1-33181619a1ad">

logistic regression used and accuracy came is 0.73

<img width="540" alt="image" src="https://github.com/user-attachments/assets/d0c19912-fc59-485d-9e8b-8486b0787ff3">


## An overview of the deployed model and instructions on how to query the endpoint with a sample input

<img width="540" alt="image" src="https://github.com/user-attachments/assets/77b6076d-a104-417d-820d-84dc75fc046f">


The deployed model setup involves the following steps:

1. **Inference Configuration**:
   - The **`InferenceConfig`** defines how the model will be served. It includes an entry script (`entry_script`) responsible for handling requests and making predictions, as well as the **environment** that specifies the required dependencies for the model to run.

2. **Deployment Configuration**:
   - The model is deployed using **Azure Container Instances (ACI)**, which allows for deploying models as web services.
   - The configuration specifies **1 CPU core** and **1 GB of memory** to allocate resources for the deployed service.
   - **Authentication** is enabled to ensure secure access to the model’s API.
   - **Application Insights** is also enabled to monitor the performance and diagnose issues with the deployed model.

3. **Model Deployment**:
   - The model is deployed as a service in the specified Azure ML Workspace (`ws`), with the name "aciservice."
   - The deployment process involves loading the model, configuring the inference environment, and creating the web service endpoint.
   - Once the deployment completes, the service becomes available for making predictions via API calls.

In summary, the model is deployed as a secure, monitored web service using ACI, with resource configurations and monitoring tools like Application Insights to track its performance.(the rest of the details will be in the screenshot setion)

<img width="540" alt="image" src="https://github.com/user-attachments/assets/ab338a2a-2133-4e49-a3b9-827f95fccbe3">





## A short overview of how to improve the project in the future

There is a noticeable difference in accuracy between the Hyperdrive and AutoML approaches. AutoML achieved an accuracy of 0.90, while Hyperdrive reached 0.73. To improve the performance of Hyperdrive, several adjustments could be made:

Use GridParameterSampling to explore a wider range of hyperparameters for better results.
Switch to a more "conservative" early stopping policy, such as MedianStoppingPolicy, to avoid prematurely halting promising runs.
Increase the max_total_runs to allow for a more extensive search across different hyperparameter combinations.
## 	ALL the screenshots required with a short description

RunDetails(run).show(): Displays a widget that shows the real-time progress of the AutoML experiment, including metrics, model status, and more within a Jupyter notebook environment.

run.get_children(): Retrieves all the individual runs or child runs of the main AutoML experiment (these represent different models trained during the AutoML process).

For loop: Iterates over each child run, printing a separator ('------') and details of each run to track their progress and results.

In summary, the code displays real-time updates of the AutoML experiment and prints the details of each individual run.


<img width="540" alt="image" src="https://github.com/user-attachments/assets/a01832f7-fbc3-4496-8666-f0cd06c6829d">

<img width="540" alt="image" src="https://github.com/user-attachments/assets/5677f506-3a94-4dec-8003-4d906b06f1d2">


also we can see the best run metrics :


<img width="540" alt="image" src="https://github.com/user-attachments/assets/77f04a08-7361-454b-9e65-bf3d995f3f97">

the best model run ID once we register it 


![image](https://github.com/user-attachments/assets/e09d2d3a-ff34-4307-b412-3d4c117b27c8)


the run details from hyperparameter tuning :


<img width="540" alt="image" src="https://github.com/user-attachments/assets/f670b98b-3b9e-4342-8f34-966cd46cfbed">

and we can see its metrics:


![image](https://github.com/user-attachments/assets/4f63969b-915a-4d1b-97f6-335ccabec776)

using cpi-cluster for the tunning



![image](https://github.com/user-attachments/assets/6295acdb-997e-4d13-a092-51c1fbeab1df)

we can see the parallel runs:


![image](https://github.com/user-attachments/assets/06a81b73-2f36-4548-81ef-08f7a312e43b)







## A link to the screencast video on YouTube (or a similar alternative streaming service)
https://www.loom.com/share/fdc930336f614a05bbfbc7a4d5af8c2a?sid=962f5b08-5a68-47a6-affa-16ecd2db9e5d




