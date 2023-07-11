# Project description

The goal of this project was to create a program that collects information about products on the first page of Jumia (an e-commerce store ) and saves this data in a table and save it on a CSV file

The idea of the program:

The user enters the search keyword that he wants to use, then the program converts this keyword into an URL then opens the source of this URL using Requests library, then collects the ( name, price, discount, price after discount, sales, and rating) for all the 2000 products that appear in the search results

steps to create this program:

- First, web scraping
In the first step, I used BeautifulSoup and Pandas to web scrap and found the HTML tags that held the data that I was looking for


- Second, creating the program
after finding the names and classes of the tags that hold the data I need, I wrote my program on my code editor, and this program contains a loop that iterates over all the HTML tags for all of the products, then saves these data on a CSV file on the desktop.
