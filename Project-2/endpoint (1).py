import urllib.request
import json
import os
import ssl
import requests


def allowSelfSignedHttps(allowed):
    # Bypass the server certificate verification on the client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)  # This line is needed if you use a self-signed certificate in your scoring service.

# Define the input data
data = {
  "Inputs": {
    "data": [
      {
        "age": 17,
        "campaign": 1,
        "cons.conf.idx": -46.2,
        "cons.price.idx": 92.893,
        "contact": "cellular",
        "day_of_week": "mon",
        "default": "no",
        "duration": 971,
        "education": "university.degree",
        "emp.var.rate": -1.8,
        "euribor3m": 1.299,
        "housing": "yes",
        "job": "blue-collar",
        "loan": "yes",
        "marital": "married",
        "month": "may",
        "nr.employed": 5099.1,
        "pdays": 999,
        "poutcome": "failure",
        "previous": 1
      },
      {
        "age": 87,
        "campaign": 1,
        "cons.conf.idx": -46.2,
        "cons.price.idx": 92.893,
        "contact": "cellular",
        "day_of_week": "mon",
        "default": "no",
        "duration": 471,
        "education": "university.degree",
        "emp.var.rate": -1.8,
        "euribor3m": 1.299,
        "housing": "yes",
        "job": "blue-collar",
        "loan": "yes",
        "marital": "married",
        "month": "may",
        "nr.employed": 5099.1,
        "pdays": 999,
        "poutcome": "failure",
        "previous": 1
      }
    ]
  }
}

# Convert data to JSON string
body = json.dumps(data).encode('utf-8')

# Define the scoring URI and API key
scoring_uri = 'https://udacity-1-imszx.northcentralus.inference.ml.azure.com/score'
key = 'u0Ezy25oNPqboQYZomkKfZiEjXKdK6YB'
if not key:
    raise Exception("A key should be provided to invoke the endpoint")

# Set up the request headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key
}

# Make the request using urllib
req = urllib.request.Request(scoring_uri, body, headers=headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print("Response from urllib request:")
    print(result.decode('utf-8'))
except urllib.error.HTTPError as error:
    print("The request failed with status code:", error.code)
    print(error.info())
    print(error.read().decode("utf-8", 'ignore'))

# Save input data to a JSON file
with open("data.json", "w") as _f:
    _f.write(json.dumps(data))

# Make the request using requests
resp = requests.post(scoring_uri, json=data, headers=headers)
print("Response from requests:")
print(resp.json())
