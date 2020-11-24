# import' packages
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navegation
chrome = webdriver.Chrome(ChromeDriverManager().install())
chrome.get('https://web.whatsapp.com/')

#scannner qrcode with cell
time.sleep(30)

#groups and contacts
groups = ['RELATORIO','Mamacos solteiros e Oziel']


#message
message = 'Hello! Welcome to my git hub'

#functions
def search_group(group):
    value_search = chrome.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    value_search.click()
    value_search.send_keys(group)
    value_search.send_keys(Keys.ENTER)

def send_messenger(message):
    value_search = chrome.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    value_search[1].click()
    time.sleep(3)
    value_search[1].send_keys(message)
    value_search[1].send_keys(Keys.ENTER)


# search groups 
for group in groups:
    search_group(group)
    send_messenger(message)