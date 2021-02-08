import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

# Read input file json
file = open('/home/kamini/Desktop/Niyuj-Assign-new/ApiAutpmation/POST_Request/createUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

#Make post request with Json Input body

response = requests.post(url,request_json)
print(response.content)

assert response.status_code == 201

# Fetch header from response
print(response.headers.get('Content-Length'))

# Parse responde to josn format
response_json = json.loads(response.text)

#Pick ID using json path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])

