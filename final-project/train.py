from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.core import Dataset, Workspace

# Define main function
def main():
    # Set up argument parsing for model hyperparameters
    parser = argparse.ArgumentParser()

    # Hyperparameters for Logistic Regression
    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    # Get the run context
    run = Run.get_context()

    # Log the hyperparameters
    run.log("Regularization Strength", float(args.C))
    run.log("Max iterations", int(args.max_iter))

    # Get the workspace from the run context
    ws = run.experiment.workspace

    # Access the dataset by name from the Azure ML workspace
    dataset = Dataset.get_by_name(ws, name='heart_failure_dataset')

    # Convert the dataset to a pandas DataFrame
    df = dataset.to_pandas_dataframe()

    # Print the first few rows of the dataset (optional)
    print(df.head())

    # Split the data into features (X) and labels (y)
    x = df[['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 
            'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 
            'sex', 'smoking', 'time']]
    y = df[['DEATH_EVENT']]

    # Split into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=0)

    # Train the Logistic Regression model
    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    # Evaluate the model
    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", float(accuracy))
    
    # Save the model to the outputs directory
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/hyper-model.pkl')

if __name__ == '__main__':
    main()
