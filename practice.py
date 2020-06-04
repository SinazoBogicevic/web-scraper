import requests

# beautiful soup allows for us to parse the page and pull out individual items from the page

from bs4 import BeautifulSoup

#enables python to send emails
import smtplib

URL = 'https://www.game.co.za/game-za/en/All-Game-Categories/Baby-%26-Toys/Baby-Travel/Buggies-%26-Strollers/Deluxe-3-Wheel-Jogger/p/00746210'

headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'} #gives info about our browser

def check_price():
    page = requests.get(URL, headers=headers) # returns all the data from the website
    # if I print(page) it will show me if permission is allowed

    #parses everything for us so we can pull out the individual pieces of information
    soup = BeautifulSoup(page.content, 'html.parser') 
    #print(soup.prettify()) #to see data

    title = soup.find("div",attrs={"class":"name"}).get_text()
    price = soup.find("span", attrs={"class": "pdp_price"}).get_text()
    initial_price = price.strip()
    string_price = initial_price[1:6]

    conversion_price = ""

    #used this to remove the ,(comma)
    for number in string_price: 
        if number.isnumeric() == True:
            conversion_price += number

    converted_price = float(conversion_price)

    print(title)
    print(converted_price)

    if(converted_price > 1300):
        send_mail()
    else:
        print("Price is still too high")

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls() #encrypts
    server.ehlo()

    server.login('snazonoqhamza94@gmail.com','pviewsimdzdvghgz') #generated password

    subject = 'Price fell down'
    body = 'Check the link ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('snazonoqhamza94@gmail.com','snoqhamza@yahoo.com', msg)    

    print("the email has been sent")

    server.quit #closes the connection

#will continously check while True using the time.sleep so every minute or whatever time i specified
''''while True:
    check_price()
    time.sleep(60)
'''

check_price()