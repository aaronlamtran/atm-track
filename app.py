import builtins
from distutils.spawn import find_executable
from email import contentmanager
import os
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from re import sub
from decimal import Decimal
from dotenv import load_dotenv
load_dotenv()

CHROME_DRIVER_PATH=os.getenv('CHROME_DRIVER_PATH') + "/chromedriver"
SWITCH_ATM=os.getenv('SWITCH_ATM_PATH')
SWITCH_PW=os.getenv('SWITCH_PW')
SWITCH_USER=os.getenv('SWITCH_USER')


chrome_options=Options()
service=Service(executable_path=CHROME_DRIVER_PATH)
driver=webdriver.Chrome(options=chrome_options, service=service)
driver.implicitly_wait(45)

driver.get(SWITCH_ATM)

user_field = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_UserName"]')
p_field = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_Password"]')
btn = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_LoginButton"]')

user_field.send_keys(SWITCH_USER)
p_field.send_keys(SWITCH_PW)

terminals = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_PageList"]/option[5]')

terminals.click()
btn.click()
content = driver.find_element(By.XPATH, '//*[@id="contentbody"]/div[2]/div')
if not content:
  try:
    agree_btn = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_Agree"]')
    agree_btn.click()
  except Exception as err:
    print(err)
    next()

t_id = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList"]/tbody/tr[2]/td[2]')
cash_balance = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList_ctl02_lblCashBalance"]')
days_until_load = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList_ctl02_lblDaysUntilCashLoad"]')
last_txn = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList"]/tbody/tr[2]/td[10]')

print('t_id.text:',t_id.text)
print('cash_balance.text:',cash_balance.text)
print('days_until_load.text:',days_until_load.text)
print('last_txn.text:',last_txn.text)

cash = Decimal(sub(r'[^\d.]', '', str(cash_balance)))
print('cash:', cash)


# time.sleep(30)
# driver.quit()
