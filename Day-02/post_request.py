import requests

url='https://jsonplaceholder.typicode.com/posts'

data={'title':'AI Engineer',
      'body':'I am learning AI Engineering',
      'userId':1}

headers={'Authorization':'Bearer YOUR_API_KEY',
         'Content_Type':'application/json'}

response=requests.post(url,headers=headers,json=data)

print(response.status_code)
print(response.json())