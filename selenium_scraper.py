from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from credentials import clientCard, passcode, headless

def rbcselenium():
  if headless:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options = chrome_options)
  else:
    browser = webdriver.Chrome()

  browser.maximize_window()
  browser.get("https://www1.royalbank.com/cgi-bin/rbaccess/rbunxcgi?F6=1&F7=IB&F21=IB&F22=IB&REQUEST=ClientSignin&LANGUAGE=ENGLISH&_ga=2.74194327.421735078.1636142251-1679506849.1636142251")

  username = browser.find_element_by_id("K1")
  username.send_keys(clientCard)
  time.sleep(0.5)
  password = browser.find_element_by_id("QQ")
  password.send_keys(passcode)
  password.send_keys(Keys.RETURN)
  time.sleep(4)

  # Chequing Account
  browser.find_element_by_link_text("RBC Day to Day Banking").click()
  rbc_chequing_html = browser.page_source
  time.sleep(2)
  browser.find_element_by_link_text("My Accounts").click()
  time.sleep(2)

  # Credit Card Account
  browser.find_element_by_link_text("RBC Rewards Visa Gold").click()
  rbc_visa_html = browser.page_source
  time.sleep(2)
  browser.find_element_by_link_text("My Accounts").click()
  time.sleep(2)
  browser.close()

  with open("/Users/marc/Documents/Development/bank_scraping/chequing_html", 'w') as file:
    file.write(rbc_chequing_html)

  with open("/Users/marc/Documents/Development/bank_scraping/visa_html", 'w') as file:
    file.write(rbc_visa_html)

  # return (rbc_chequing_html, rbc_visa_html)

rbcselenium()