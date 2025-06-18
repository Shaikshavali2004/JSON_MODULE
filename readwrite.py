import json

fp1=open('emp.json','r')
fp2=open('users.json','w')

users=json.load(fp1)
print(type(users))

json.dump(users,fp2)
print("New File Created!")
fp2.close()
fp1.close()

