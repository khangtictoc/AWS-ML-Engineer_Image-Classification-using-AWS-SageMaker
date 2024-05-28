import os

# Check if an environment variable exists
if os.environ.get('VARIABLE_NAME') == None:
    print("The environment variable does not exist.")
else:
    print("The environment variable exists.")