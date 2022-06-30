#! python3
# Syntax of the code to run = 'python commandLineEmailer.py [emailAddress] [userPassword] [email content]'
# PLEASE NOTE - CSS SELECTORS SUBJECT TO CHANGE IF THE HTML IS AMENDED BY THE H0ST
import sys, pyperclip, time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

# Take an email address and string of text from the command line
if len(sys.argv) > 1:
	# Get address from command line
	emailAddress = ' '.join(sys.argv[1:2])
else: # Get address from clipboard
	emailAddress = pyperclip.paste()

if len(sys.argv) > 2:
	userPassword = ' '.join(sys.argv[2:3])
else:	
	userPassword = pyperclip.paste()

if len(sys.argv) > 3:
	emailContent = ' '.join(sys.argv[3:])
else:
	emailContent = pyperclip.paste()

# Log into email account shaw51@hotmail.co.uk
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://outlook.live.com/')
linkElem = browser.find_element(By.LINK_TEXT, 'Sign in')
linkElem.click()

#  Username
time.sleep(1)
linkElem = browser.find_element(By.ID, 'i0116')
linkElem.send_keys(emailAddress) # This will be the stored username from the terminal
linkElem = browser.find_element(By.ID, 'idSIButton9')
linkElem.click()

#  Password
time.sleep(1)
linkElem = browser.find_element(By.ID, 'i0118')
linkElem.send_keys(userPassword) # This will be stored from the argument within the termina
linkElem = browser.find_element(By.ID, 'idSIButton9')
linkElem.click()

# 'Stay signed in' prompt
time.sleep(1)
linkElem = browser.find_element(By.ID, 'idBtn_Back')
if linkElem.is_displayed() == True:
	linkElem.click()
else:
	pass

# New message
time.sleep(4)
linkElem = browser.find_elements(By.CLASS_NAME,'ms-Button-label')[1]
linkElem.click()

# Add recipient
time.sleep(4)
linkElem = browser.find_element(By.CLASS_NAME, 'QdX2d')
linkElem.click()
linkElem.send_keys(emailAddress)

# Add email body content
linkElem = browser.find_element(By.CLASS_NAME, 'dbf5I')
linkElem.click()
# linkElem.send_keys('Hello automation test') 
linkElem.send_keys(emailContent) # This will be stored from the argument within the terminal or from copied text
time.sleep(1)

# Find the send button
linkElem = browser.find_elements(By.CLASS_NAME,'ms-Button--primary')[0]
linkElem.click()	

# Send without subject prompt
linkElem = browser.find_element(By.ID,'ok-1')
linkElem.click()

time.sleep(2)
browser.close()
