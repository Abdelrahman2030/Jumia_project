'''
This version is the updated version, in the first version the user have to input an url of a certain 
product on jumia and the program would give him the name, price, discount, final price, ratings, 
and number of ratings, 

this updated version the user enter a search key word and the program takes this key words creats a jumia 
link for the first page that will appear in search results and collect name, price, discount, 
final price, rating, and shipping of all the products in the first page and put all of these data 
in a data frame
'''

import pandas as pd
from bs4 import BeautifulSoup
import requests

key_word = input("Please write your search key word: ")

url_key_word = key_word.replace(" ", "+")
url = "https://www.jumia.com.eg/catalog/?q={}".format(url_key_word)

content = requests.get(url).content
soup = BeautifulSoup(content, "lxml")

'''
This program is the final product all of the web scraping process is in jupyter notebook
'''

# create a list with all of <div> tags that has the data of the product inside of it
div_list = soup.find_all("div", class_ = "info")

#Empty lists for the values
names_list = []
old_prices_list = []
new_prices_list = []
discount_list = []
rating_list = []

for div in div_list:
    product_name = div.find("h3", class_ = "name").contents[0]
    
    price = div.find("div", class_ = "prc").contents[0]
    #I want to remove the EGP and "," to make it float
    price = price.split()[1]
    price = float(price.replace(",",""))
    try:
        old_price = div.find("div", class_ = "old").contents[0]
        old_price = old_price.split()[1]
        old_price = float(old_price.replace(",",""))
    except:
        old_price = price
    
    try:
        discount = div.find("div", class_ = "bdg _dsct _sm").contents[0]
        discount = int(discount.replace("%", ""))
    except:
        discount = 0
    
    try:
        rating = div.find("div", class_ = "stars _s").contents[0]
        rating = float(rating.split()[0])
    except:
        rating = "No rating"
        

    
    #Now i will append these values into new lists
    
    names_list.append(product_name)
    old_prices_list.append(old_price)
    new_prices_list.append(price)
    discount_list.append(discount)
    rating_list.append(rating)
    


#Nowi will create the data frame
dict_ = {"product_name": names_list, "old_price": old_prices_list, "discount": discount_list, 
         "current_price": new_prices_list,
         "rating": rating_list}

df = pd.DataFrame(dict_)

print(df.head())

df.to_csv("{} data set.csv".format(key_word), index = False)