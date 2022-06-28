#! python3
# Play the 2048 game on https://gabrielecirulli.github.io/2048/ using automation

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Navigate to website
# browser = webdriver.Chrome() # Opens Chrome using Selenium
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # Opens Firefox using Selenium
url = 'https://gabrielecirulli.github.io/2048/'
browser.get(url)

# Navigate cookies popup
time.sleep(1)
linkElem = browser.find_element(By.ID, 'ez-accept-all')
linkElem.click()

# input key presses. Use 'html' tag as this is the base tag for websites
htmlElem = browser.find_element(By.TAG_NAME, 'html')

# Create a loop to continuously input keys until game has been won
i = 0
while i < 10:
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)

	try:
		retryElem = browser.find_element(By.LINK_TEXT, 'Try again')
		retryElem.click()
		i += 1
		print(i)
	except:
		pass






