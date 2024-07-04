### The pipeline architecture, including data, hyperparameter tuning, and classification algorithm  

The architecture of the pipeline includes various components such as data handling, adjusting hyperparameters, and selecting the classification algorithm. I use Logistic Regression algorithm from the SKLearn framework and utilize hyperDrive for optimizing hyperparameters.
The pipeline consists of the following sequential steps:
1.	Data Collection: I retrieve the dataset using TabularDatasetFactory from the source provided by udacity. 
2.	Data Cleaning: removing missing value and do one hot encoding for feature engineering. 
3.	Data Splitting: I use 70% for training split and 30% for test. 
4.	Hyperparameter Sampling: Hyperparameters are dynamic settings that influence the training process. For each training cycle, hyperDrive manages this step. Steps:
•	Hyperparameter Selection: I optimize 'C' (inverse of regularization strength) and 'max_iter' (maximum number of iterations for convergence). I explore these hyperparameters through random sampling from set values: C values are [1,2,3,4,5] and max_iter values range from 80 to 200.Random sampling tested different combinations. 
5.	Model Training: With  datasets prepared and hyperparameters set, we proceed to train the Logistic Regression model.
6.	Model Testing: using accuracy metric for evaluation the model tested on train split. 
7.	Early Stopping Policy Evaluation: BanditPolicy being used with these config :
Evaluation Interval: 1 - The policy evaluates the model's performance after every iteration.
Slack Factor: 0.2 - The model needs to achieve at least 80% of the performance of the best metric observed so far to avoid termination.
Delay Evaluation: 5 - The policy starts applying its rules after the first 5 iterations, allowing models a grace period to stabilize before making any termination decisions.
In essence, starting from the sixth iteration, the policy checks each model's performance every iteration, and terminates those that fall below 80% of the best observed metric. This ensures efficient use of computational resources by focusing on more promising model configurations.
8.	Saving the Model: Once training is complete, the model is saved . 
Steps 1-3 and 5,6,8 is accessible through train.py and 4 and 7 are for hyperdrive part which is in udacity project.ipynb
### Auto ML
The result/code store in AutoML.ipynb. I defined exit criterion to stop the training which ensures that resources are not used once the goal has been met.
These are what I used in the AutoMl notebook

    task='classification',
    primary_metric='accuracy',
    training_data=dataset,  
    label_column_name='y',
    n_cross_validations=5,
    compute_target=compute_target



This is alos used to delete the cluster 
from azureml.core import Workspace
from azureml.core.compute import ComputeTarget

Load the workspace
ws = Workspace.from_config()

Get the compute target
compute_target = ws.compute_targets['cpu-cluster-small']

 Delete the compute target
compute_target.delete()


It turns out the xgboost classifer has the best performance than the others, the reason that some model perform better than the other could be due to different reasons : differences in how they handle data, regularization, and tree construction algorithms, AutoML frameworks often tune hyperparameters. Different settings might be more optimal for certain models, leading to better performance. Training Time: Longer training times (e.g., 0:03:03 for XGBoost) might allow more thorough exploration of hyperparameter space, leading to better performance but also indicates more computational resources used.
### Conclusion :
consistent high performance of XGBoostClassifier and LightGBM models across different preprocessing steps highlights their robustness and suitability for the dataset. Preprocessing steps like MaxAbsScaler and StandardScalerWrapper further enhance model performance by ensuring data is appropriately scaled.

### Pipeline comparison
The model generated by AutoML had accuracy slighlty higher than the HyperDrive model. 0.9124f or autoML and 0.9168.
The Auto ml has access to different algortihms than hyper drive. 
 for HyperDrive The architecture is different as hyperDrive was restricted to Logistic Regression from SKLearn, whereas AutoML has access to wide variety of algorithms.
In certain situations, a particular model might not be the optimal choice. This disadvantage affects HyperDrive, as it relies on user-selected models, unlike AutoML, which automates model selection. Consequently, the variation in accuracy is justifiable.
### Future work
## Improvements for hyperdrive
Utilize Bayesian Parameter Sampling for smarter hyperparameter selection and consider alternative primary metrics to better assess model performance. Increase the total runs to explore more combinations, acknowledging the potential cost impact.
## Improvements for autoML
Extend the experiment timeout to allow for more model experimentation, though this may increase costs. Use alternative primary metrics to better assess model performance. Increase cross-validations to reduce bias, and address the class imbalance to improve overall model accuracy.

