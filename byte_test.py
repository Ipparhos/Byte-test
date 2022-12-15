def main():
    import requests
    import json
    from columnar import columnar

    BASE_URL = 'https://dummyjson.com'
    def request_to_dict (url):
        response_products = requests.get(f"{url}/products")

        response_categories = requests.get(f"{url}/products/categories")


        #Making responses into a dictionary
        data_products = response_products.json()
        data_categories = response_categories.json()

        #Checking that data is actually a dictionary
        return data_products, data_categories


    def finding_most_expensive_product(data_products, data_categories):
        stats = []
        for categorie in data_categories:
            most_expensive_product = 0
            stock_of_product = 0
            for product in data_products["products"]:
                if product["category"] == categorie:
                    stock_of_product += product['stock']
                    if most_expensive_product < product['price']:
                        most_expensive_product = product['price']
                        categorie_of_product = categorie
                        title_of_product = product['title']
            
            if most_expensive_product != 0:
                stats.append([categorie_of_product, title_of_product, most_expensive_product, stock_of_product])
        return stats
    

    def write_table(stats):
        # Formating the stats into a more readable table            
        headers = ['CATEGORY', 'MOST EXPENSIVE PRODUCT', 'PRICE', 'CAT STOCK']
        table = columnar(stats, headers)

        with open('stats.txt', 'w') as f:
            f.write(table)
        f.close()
    
    def value_of_most_expensive_product(stats):
        most_expensive_of_all = int(stats[0][2])
        for i in stats:
            if int(i[2]) > most_expensive_of_all:
                most_expensive_of_all = int(i[2])
                item_description = i
        print(f"The price of the most expensive item is {item_description[2]}")
    
    data_products, data_categories = request_to_dict(BASE_URL)
    stats = finding_most_expensive_product(data_products, data_categories)
    write_table(stats)
    value_of_most_expensive_product(stats)

if __name__ == "__main__":
    main()