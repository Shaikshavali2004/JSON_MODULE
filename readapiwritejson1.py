# #Extract from API sources

# import requests,json

# api_url='https://dummyjson.com/products'
# data=requests.get(api_url)
# product_data=data.json()
# print(type(product_data))
# products=product_data['products']
# print(type(products))

# #Transform data

# beauty_products=[]
# for product in products:
#     if product['category']=='beauty':
#         beauty_products.append(product)

# print(len(beauty_products))


# #Load into json file

# fp=open('beauty_products.json','w')
# json.dump(beauty_products,fp,indent=2)

# print("New File Created: beauty_products.json")

# fp.close()





#Extract from API sources

import requests,json

api_url='https://dummyjson.com/products'
data=requests.get(api_url)
product_data=data.json()
print(type(product_data))
products=product_data['products']
print(type(products))

#Transform data

beauty_products=[]
for product in products:
    if product['category']=='beauty':
        beauty_products.append({"id":product['id'],"name":product['title'],"type": product['category'],"price":product['price']})

print(len(beauty_products))


#Load into json file

fp=open('beauty_products.json','w')
json.dump(beauty_products,fp,indent=2)

print("New File Created: beauty_products.json")

fp.close()
