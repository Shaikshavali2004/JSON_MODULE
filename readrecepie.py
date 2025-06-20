# Extracting data from a dummy API and saving it to a JSON File.
import requests,json
api_url = 'https://dummyjson.com/recipes'
data=requests.get(api_url)
recepie_data=data.json()
print(type(recepie_data))
recipes=recepie_data['recipes']
print(type(recipes))

#Transform data
recepie_items = []
for item in recepie_items:
    recepie_items.append(item)

print(len(recepie_items))


#Load into json file
fp=open('recepie_items.json','w')
json.dump(recepie_items,fp)

print("New File Created: recepie_items.json")
fp.close()


