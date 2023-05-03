import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas
import time

driver = webdriver.Chrome()

cityList = ["Antalya","Isparta","Burdur","Denizli"]

textOutput = ""

for i in cityList:
    driver.get("https://tr.wikipedia.org/wiki/"+i)
    content = driver.find_element(By.ID,value="mw-content-text").text
    textOutput += "City Name :"+i+"\n"
    textOutput += "City Information : "+content+"\n"
    textOutput += "--------------------------------------------------\n"
    time.sleep(1)

#save textOutput to a file
with open("cityInfo.txt","w",encoding="utf-8") as file:
    file.write(textOutput)



