import requests

url = "http://216.10.245.166/Library/GetBook.php"

# get api method to retrieve book details
response = requests.get(url,params={'AuthorName': 'xyzabc'})
json_response = response.json()
print(json_response)
print(response.status_code)
assert response.status_code == 200