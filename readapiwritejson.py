import requests,json

api_url='https://jsonplaceholder.typicode.com/users'

data=requests.get(api_url)
users=data.json()
print(type(users))

fp=open('new_users.json','w')
json.dump(users,fp)

print("New File Created")

fp.close()