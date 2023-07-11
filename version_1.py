# you give this program the url of any Jamuia product, it will give
#the name, the price, the discount, the value after discount, the rating, the num of rating

import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://www.jumia.com.eg/am-shop-bundle-of-4-socks-19933857.html"


content = requests.get(url).content
soup = BeautifulSoup(content, "lxml")

# the name of the product
title = soup.find("title")
title = title.contents[0]
print("the name of the product is ", title)

# original price
original_price = soup.find("span", class_ = "-tal -gy5 -lthr -fs16")
original_price = original_price.contents[0]
original_price = original_price[4: ]
print("the price is {} EPG".format(original_price))

# the discount on the product
discount = soup.find("span", class_ = "bdg _dsct _dyn -mls")
discount = discount.contents[0]
discount = discount.replace("%", "")
discount = int(discount)
print("the discount is {} % ".format(discount))

# price after discount

after_price = soup.find("span", class_ = "-b -ltr -tal -fs24")
after_price = after_price.contents[0]
after_price = after_price[4: ]
print("the price after discount is {} EPG".format(after_price))

# the total rating
total_rating = soup.find("div", class_ = "stars _s _al")
total_rating = total_rating.contents[0]
total_rating = total_rating[:3]
print("the rating is {} out of 5".format(total_rating))

# num of rating
num_rating = soup.find("a", class_ = "-plxs _more")
num_rating = num_rating.contents[0]
num_rating = num_rating[1: 3]
print("the number of reviews is" ,num_rating)


