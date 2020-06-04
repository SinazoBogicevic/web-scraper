import pandas as pd
import time

# requests allows me to access url and pull out data from that page
import requests

# allows me to parse a page and pull out information from that page
from bs4 import BeautifulSoup

# allows python to send emails
import smtplib

URL = 'https://remote.co/international-remote-jobs/'

# my agent that gets me onto the internet
headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# lets me know if i can proceed
page = requests.get(URL, headers=headers)

if page.status_code == 503:  # status_code returns only the no. e.g 03, 402 etc
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
# #print(soup.prettify()) #see how elements are nested in html

job_info = soup.find("div", attrs={"class": "position"})

print("Job information: {}".format(job_info))

"""
for matchDiv in soup.find("div", attrs={"class": "position"}):
    #print(matchDiv)
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


print(company_name)
