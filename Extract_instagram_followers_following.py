from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url = "https://www.instagram.com/guviofficial/"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(2)

# find the followers webelements 
webelement_of_followers = driver.find_element(By.XPATH, "(//span[@class='_ac2a'])[2]").get_attribute("title")
print(f"No of followers : ", {webelement_of_followers})

# find the following webelements 
webelement_of_following = driver.find_element(By.XPATH, "(//span[@class='_ac2a'])[3]").text
print(f"No of following : ", {webelement_of_following})