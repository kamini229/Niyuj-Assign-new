import json

import jsonpath
import requests

url = "https://reqres.in/api/users/2"

# Read input file json
file = open('/home/kamini/Desktop/Niyuj-Assign-new/ApiAutpmation/POST_Request/createUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response = requests.put(url,request_json)
print(response.content)

assert response.status_code == 200

