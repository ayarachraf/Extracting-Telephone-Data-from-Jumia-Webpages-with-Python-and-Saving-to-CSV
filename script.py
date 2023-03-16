from bs4 import BeautifulSoup
import requests 
import csv
from itertools import zip_longest

titles = []
prices = []
images = []

for a in range(50):
    request = requests.get(f"https://www.jumia.ma/telephone-tablette/?page={a}#catalog-listing")
    src = request.content
    soup = BeautifulSoup(src , "lxml")
    product_title = soup.find_all("h3" , {"class":"name"})
    product_price = soup.find_all("div" , {"class":"prc"})
    product_images = soup.find_all("img" , {"class": "img"})

    # Create a new list to store the image URLs
    image_urls = []
    for img in product_images:
        src = img.get("src")
        image_urls.append(src)

    # Append the data to the main lists
    for i in range(int(len(product_title))):
        titles.append(product_title[i].text)
        prices.append(product_price[i].text)
        images.append(image_urls[i])

# Write the data to a CSV file
with open("/home/achrafayar/Documents/webScaping/Jumia/telephones.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Image"])
    for row in zip_longest(titles, prices, images):
        writer.writerow(row)







    





