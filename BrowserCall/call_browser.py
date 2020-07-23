from selenium import webdriver
import os
path = "./chromedriver/chromedriver"
os.environ['webdriver.chrome.driver'] = path
driver = webdriver.Chrome(path)
driver.get("https://www.google.co.in/")
