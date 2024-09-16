import requests
import json

# URL for the web service, replace with your actual scoring URI
scoring_uri = 'http://29d633d1-aec3-432a-b6d2-02a5a7ede050.northcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'YxaJXA3AVkNIZptXa2Ld55VCN7DmdL3h'

# Correct the data structure by adding 'Inputs' and 'GlobalParameters'
data = {
    "Inputs": {
        "data": [
            {
                "age": 51, 
                "anaemia": 0, 
                "creatinine_phosphokinase": 582, 
                "diabetes": 0, 
                "ejection_fraction": 20, 
                "high_blood_pressure": 1, 
                "platelets": 265000, 
                "serum_creatinine": 1.9, 
                "serum_sodium": 130, 
                "sex": 0, 
                "smoking": 0,
                "time": 4
            },
            {
                "age": 25, 
                "anaemia": 0, 
                "creatinine_phosphokinase": 1380, 
                "diabetes": 1, 
                "ejection_fraction": 25, 
                "high_blood_pressure": 1, 
                "platelets": 271000, 
                "serum_creatinine": 0.9, 
                "serum_sodium": 130, 
                "sex": 1, 
                "smoking": 0,
                "time": 38
            }
        ]
    },
    "GlobalParameters": {
        "method": "predict"  # This can be "predict" or "predict_proba"
    }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
print("++++++++++++++++++++++++++++++")
print("Expected result: [true, true], where 'true' means '1' as result in the 'DEATH_EVENT' column")
