# importing libraries
from bs4 import BeautifulSoup
import requests


def main(URL):
    # opening our output file in append mode
    File = open("out.csv", "a")

    # specifying user agent, You can use other user agents
    # available on the internet
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # retrieving product url
    try:
        a = soup.find('a', attrs={"class": 'a-size-base a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal'})
        if(a):
            url = a['href']
        else:
            url = "NA"
    except AttributeError:
        url = "NA"
    print(f"Product Url = https://www.amazon.in{url}")
    File.write(f"{url},")

    # retrieving product name
    try:
        name = soup.find("span", attrs={"class": 'a-size-medium a-color-base a-text-normal'}).string.strip().replace(',', '')
    except AttributeError:
        name = "NA"
    print("Product Name = ", name)
    File.write(f"{name},")

    # retrieving product price
    try:
        a = soup.find('a', attrs={"class": 'a-size-base a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal'})
        if(a):
            url = a['href']
        if(url):
            price = a.find("span", attrs={"class": 'a-price-whole'}).text
        else:
            price = soup.find("span", attrs={"class": 'a-price-whole'}).text
    except AttributeError:
        price = "NA"
    print("Products Price = ", price)
    File.write(f"{price},")

    # retrieving product rating
    try:
        b = soup.find('div', attrs={"class": 'a-row a-size-small'})
        if(b):
            rating = b.find("span", attrs={"class": 'a-size-base puis-normal-weight-text'}).text
        else:
            rating = soup.find("span", attrs={"class": 'a-size-base puis-normal-weight-text'}).text        
    except AttributeError:
        rating = "NA"
    print("Products Rating = ", rating)
    File.write(f"{rating},")

    # retrieving product reviews
    try:
        reviews = soup.find("span", attrs={"class": 'a-size-base s-underline-text'}).text
    except AttributeError:
        reviews = "NA"
    print("Products Reviews = ", reviews)
    File.write(f"{reviews},")

    # closing the file
    File.close()


if __name__ == '__main__':   
    main('https://www.amazon.in/s?k=bags&page=3&crid=2M096C61O4MLT&qid=1694448990&sprefix=ba%2Caps%2C283&ref=sr_pg_3')
