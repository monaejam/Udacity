from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Load the workspace configuration from the current working directory
ws = Workspace.from_config()

# Set with the deployment name
name = "aciservices"  # Your actual service name

# Load the existing web service
service = Webservice(name=name, workspace=ws)

# Enable Application Insights for detailed logging (optional)
service.update(enable_app_insights=True)

# Retrieve the logs from the service
logs = service.get_logs()

# Print each line of the logs
for line in logs.split('\n'):
    print(line)
