#consume Rest API write user data[uid,uname,age] in new csv file users.csv.

import requests, csv

api_url = 'https://dummyjson.com/users'
data = requests.get(api_url)
user_data = data.json()
print(type(user_data))

users=user_data['users']
print(type(users))
print(len(users))

users_data =[]
for user in users:
    users_data.append([user['id'],user['firstName'],user['age']])
# print(users_data)

fp=open('users.csv','w',newline='')
csv_writer = csv.writer(fp)
csv_writer.writerow(['uid','uname','age'])
csv_writer.writerows(users_data)

print('New csv file created')

fp.close()