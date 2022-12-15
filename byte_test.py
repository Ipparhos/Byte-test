import requests
import json
from columnar import columnar

BASE_URL = 'https://dummyjson.com'

response_products = requests.get(f"{BASE_URL}/products")
#print(response_products.json())

response_categories = requests.get(f"{BASE_URL}/products/categories")
#print(response_categories.json())

#Making responses into a dictionary
data_products = response_products.json()
data_categories = response_categories.json()

#Checking that data is actually a dictionary
print(type(data_products),type(data_categories))
# print(data_products)

# print(data_products["products"][1]["category"])

#Finding the most expensive product
stats = []
for categorie in data_categories:
    most_expensive_product = 0
    for product in data_products["products"]:
        if product["category"] == categorie:
            if most_expensive_product < product['price']:
                most_expensive_product = product['price']
                categorie_of_product = categorie
                stock_of_product = product['stock']
                title_of_product = product['title']
    
    if most_expensive_product != 0:
        stats.append([categorie_of_product, title_of_product, most_expensive_product, stock_of_product])

# Formating the stats into a more readable table            
headers = ['CATEGORY', 'MOST EXPENSIVE PRODUCT', 'PRICE', 'CAT STOCK']
table = columnar(stats, headers)
# print(table)

with open('stats.txt', 'w') as f:
    f.write(table)
f.close()

most_expensive_of_all = int(stats[0][2])
for i in stats:
    if int(i[2]) > most_expensive_of_all:
        most_expensive_of_all = int(i[2])
        item_description = i
print(f"The price of the most expensive item is {item_description[2]}")