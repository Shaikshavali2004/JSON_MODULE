
import json

fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))
print(employees)

for emp in employees:
     print(emp['ename'])
