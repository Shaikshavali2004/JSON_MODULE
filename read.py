# CSV: comma separated values

import csv 
fp=open('emp.csv','r')
employees=csv.reader(fp)
print(type(employees))

# for emp in employees:
#     print(emp[0], emp[1], emp[2])
#     # print(emp[1])
#     # print(emp[2])

for emp in list(employees)[1:]:
    # print(emp)
    print(emp[1])

fp.close()