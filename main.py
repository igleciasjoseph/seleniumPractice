from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from pymsgbox import *
import os, json, getpass, time

chrome_options = Options()
chrome_options.add_argument('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
chrome_options.add_argument("--kiosk")


browser = webdriver.Chrome(chrome_options=chrome_options)


def getImage():
    browser.get('https://www.google.com')
    userInput = input('Please enter something to search ')
    userChoice = input('Choices are (all, news, videos, images, and books) ')

    search = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(1)
    search.send_keys(userInput)
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    if (userChoice == 'all'):
        elem = browser.find_element_by_link_text("All").click()
    if (userChoice == 'news'):
        elem = browser.find_element_by_link_text("News").click()
    if (userChoice == 'videos'):
        elem = browser.find_element_by_link_text("Videos").click()
    if (userChoice == 'images'):
        elem = browser.find_element_by_link_text("Images").click()
    if (userChoice == 'books'):
        elem = browser.find_element_by_link_text("Books").click()
    





getImage()
time.sleep(3)
alert(text='Shutting Down', title='Sorry', button='OK')
time.sleep(1)
browser.quit()