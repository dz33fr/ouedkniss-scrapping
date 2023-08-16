# Abdelhafid BOUSLAHI
# wacim.bf@gmail.com
from time import sleep
import pandas as pd 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.ouedkniss.com/automobiles/1?hasPrice=true&marque-voiture=dacia&modele=dacia-sandero')
print("Opened Ouedkins...")

file_out  = open("data_brute_2.txt", "w+", encoding="utf-8")
i = 0
while True :
    print("cliquez sur une nouvelle annonce")
    time.sleep(5)
    infos = driver.find_element(By.CLASS_NAME, "container")

    print("{} => {}".format(i, infos.text))

    file_out.write("{}\n".format(infos.text))
    
    i +=1

    

    

    

file_out.close(500)