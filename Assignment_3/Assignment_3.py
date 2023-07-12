# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.apple.com/ca/")
time.sleep(3)

# Select Mac from the menu
click_mac = driver.find_element("xpath","//*[@id='globalnav-list']/li[2]/div/div/div[2]/ul/li[1]/a")
click_mac.click()
# Waiting for the results to load
time.sleep(2)

# Selecting a macbook from the search results
macbook_link = driver.find_element("xpath","//*[@id='chapternav']/div/ul/li[1]/a")
macbook_link.click()
# Waiting for the laptop details page to load
time.sleep(5)

# Select Macbook Air type
macbook_type = driver.find_element("xpath","//*[@id='chapternav']/div/ul/li[2]/a")
macbook_type.click()
# Waiting for the update
time.sleep(5)

# Proceed for buying macbook
click_buy = driver.find_element("xpath", "//*[@id='ac-localnav']/div/div[2]/div[2]/div[2]/div[2]/a")
click_buy.click()
time.sleep(5)

# search for macbook
search_bar = driver.find_element("id","globalnav-menubutton-link-search")
search_bar.send_keys("macbook pro m1")
time.sleep(5)
# Submitting the search query
search_bar.send_keys(Keys.RETURN)
time.sleep(5)


# Closing the webdriver
driver.close()
