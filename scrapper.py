from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get(START_URL)
time.sleep(10)
planets_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
starttable = soup.find("table")
temp_list = []
tablerows = starttable.find_all("tr")

for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

starnames = []
distance = ()
mass = ()
radius = []
lum = []

for i in range (1, len(temp_list)):
    starnames.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(starnames,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

df2.to_csv("chirag.csv")









