# requests allows me to access url and pull out data from that page
import requests

# allows me to parse a page and pull out information from that page
from bs4 import BeautifulSoup

# import panda library and numpy
import pandas as pd
import numpy as np

# allows python to send emails Simple Mail Transfere Protocol
import smtplib

URL = 'https://remote.co/international-remote-jobs/'

# my agent that gets me onto the internet
headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def scraper():

    # lets me know if i can proceed

    page = requests.get(URL, headers=headers)

    if page.status_code == 503:
        print("this is forbidden")
    elif page.status_code == 404:
        print("page not found")
    elif page.status_code == 500:
        print("internal server error")
    elif page.status_code == 200:
        print("might be okay proceed")
    else:
        print("page: {}\npage type:{} ".format(page, type(page)))

    # pulls out the individual pieces of information

    soup = BeautifulSoup(page.content, "html.parser")  # beautifulSoup object

    # print(soup.prettify()) #see how elements are nested in html

    # job_info = soup.find("div", attrs={"class": "position"})

    # print("Job information: {}".format(job_info))

    """
    for matchDiv in soup.find("div", attrs={"class": "position"}):
       print(matchDiv)
    """

    # get the link
    # get the position
    # get the company's name
    # might need classes/constructor or just dictionary
    # use panda or other to create a table for the listings

    job_titles = []

    for position in soup.find_all("h3"):
        job_titles.append(position.get_text())

    # print(job_titles)
    # print("\n")

    company_name = []

    for company in soup.find_all("div", attrs={"class": "company"}):
        company_name.append(company.findChild().text)

    data = {
        'Company': company_name,
        'Position': job_titles,
    }

    df = pd.DataFrame(data)

    try:
        # used for connecting with the server
        server = smtplib.SMTP("smtp.gmail.com", 587)

        # can identify self using ehlo()
        server.ehlo()

        # required by gmail
        server.starttls

        server.ehlo()

        server.login('snazonoqhamza94@gmail.com', 'pviewsimdzdvghgz')

        heading = "List of Remote jobs "
        link = "Click on the url to go to the website\n" + URL
        table = df

        message = "{}\n{}\n{}".format(heading, link, table)
        server.sendmail('snazonoqhamza94@gmail.com',
                        'snoqhamza@yahoo.com', message)
        print("Mail has been sent")
    except:
        print("Still not sending")

    # closes server or connection
    server.close()


scraper()
