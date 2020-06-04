import requests

# beautiful soup allows for us to parse the page and pull out individual items from the page

from bs4 import BeautifulSoup

URL = 'https://www.aliexpress.com/item/32954103946.html?spm=2114.search0603.3.1.2b051a5egGldpf&s=p&ws_ab_test=searchweb0_0%2Csearchweb201602_4_10065_10068_319_10059_10884_317_10887_10696_321_322_10084_453_10083_454_10103_10618_10307_537_536%2Csearchweb201603_52%2CppcSwitch_0&algo_expid=698d2492-7b67-49b4-ab9e-43d1e12a61e4-0&algo_pvid=698d2492-7b67-49b4-ab9e-43d1e12a61e4&transAbTest=ae803_3'

headers = {"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'} #gives info about our browser

page = requests.get(URL, headers=headers) # returns all the data from the website
# if I print(page) it will show me if permission is allowed

#parses everything for us so we can pull out the individual pieces of information
soup = BeautifulSoup(page.content, 'html.parser') 
#print(soup.prettify()) #to see data

title = soup.find("div",attrs={"class":"product-title"})

print(title)