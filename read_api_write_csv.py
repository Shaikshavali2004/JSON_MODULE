#Extract quotes from an api and write them to a CSV file.

import requests, csv
data=requests.get('https://dummyjson.com/quotes')
quotes_data = data.json()
print(type(quotes_data))

quotes = quotes_data['quotes']
print(type(quotes))

#Transform 

new_quotes = []
for quote in quotes:
    new_quotes.append([quote['id'], quote['quote'], quote['author']])
print(len(new_quotes))

#Load to CSV

fp=open('new_quotes.csv','w',newline='', encoding='utf-8')
csv_writer = csv.writer(fp,)
csv_writer.writerow(['id','quote','author'])
csv_writer.writerows(new_quotes)

# alternative way to load to csv file using 'with' statement

# with open('new_quotes.csv','w',newline='', encoding='utf-8') as fp:
#     csv_writer = csv.writer(fp,)
#     csv_writer.writerow(['id','quote','author'])
#     csv_writer.writerows(new_quotes)


print("New CSV file created with quotes data")

fp.close()

