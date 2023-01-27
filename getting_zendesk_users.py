# This script's goal is to get all the users email that we already have
# in Zendesk.
# This script take a lot of time even with the right logic. Some new reserch is needed. 

import os
from urllib.parse import urlencode
import requests


# Load the Zendesk User and the API Key from the ".env" file localizated within the same folder. 
with open(".env") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

# Access the user.
user = os.getenv("USER")

# Access the API key.
pwd = os.getenv("API_KEY")

subdomain = "" # You know which is this value. It's like "acme". In generally, it's the name of your company.

# Set the URL for search users in Zendesk.
url = f'https://{subdomain}.zendesk.com/api/v2/users.json?page[size]=100'
user = user + '/token'

# Do the HTTP get request with try/except.
try:
    response = requests.get(url, auth=(user, pwd))
except:
    print("Something in the URL call or in the requests module is wrong. Please check them.")
    exit()

# Check for HTTP codes other than 200.
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data.
data = response.json()

users = [] # Here we'll save the user found in ZD.
flag = 0

while flag < 4861: # Total pages are 4861. You can check this value by looking at the URL endpoint directly in the browser. 

# while (data["meta"]["has_more"]) == True: # Validating the pagination to check if there is more pages to look for. https://developer.zendesk.com/api-reference/introduction/pagination/#:~:text=%22next%22-,Repeat,-the%20above%20steps
    if data: # The following code will run only if data variable already has some data.
        users.append(data["users"])

        url = data["links"]["next"] # Generating the new URL for the next page with data. 

        # Do the HTTP get request with try/except.
        try:
            response = requests.get(url, auth=(user, pwd))
        except:
            print("Something in the URL call or in the request module is wrong. Please check them.")
            exit()

        # Check for HTTP codes other than 200.
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Decode the JSON response into a dictionary and use the data.
        data = response.json()

    else:
        print("Check the data variable")
    
    flag += 1

# Saving the ZD users in a text file.
with open('zd_users.txt', 'w') as f:
    f.write(str(users))