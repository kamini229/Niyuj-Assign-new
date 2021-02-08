import requests

#API url
url = "https://reqres.in/api/users?page=2"


# Send get request
response = requests.get(url)
print(response.content)
print(response.headers)