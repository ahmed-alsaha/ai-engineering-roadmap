import requests
url='https://jsonplaceholder.typicode.com/users'

response=requests.get(url)

print(response.status_code)

data=response.json()
print(len(data))
for record in data :
    print(record['name'])