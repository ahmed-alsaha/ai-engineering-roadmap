import requests

url1='https://jsonplaceholder.typicode.com/users'

response1=requests.get(url1)
print(response1.status_code)
users_data=response1.json()
for record in users_data:
    print(record['name'])
    
url2='https://jsonplaceholder.typicode.com/posts'

data={
    'message' :'What is Machine Learning ?'   
}    

response2=requests.post(url2,json=data)

print(response2.status_code)

print(response2.json())