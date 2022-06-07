from cgitb import text
from distutils.spawn import find_executable
from email import contentmanager
import os
import re
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
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from controllers import email_one, get_all, post_one
load_dotenv()


startTime = time.time()
print('working...')


CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH') + "/chromedriver"
SWITCH_ATM = os.getenv('SWITCH_ATM_PATH')
SWITCH_PW = os.getenv('SWITCH_PW')
SWITCH_USER = os.getenv('SWITCH_USER')

chrome_options = Options()
chrome_options.headless = True
service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.implicitly_wait(25)
def main():
    driver.get(SWITCH_ATM)

    user_field = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_UserName"]')
    p_field = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_Password"]')

    user_field.send_keys(SWITCH_USER)
    p_field.send_keys(SWITCH_PW)

    terminals = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_PageList"]/option[5]').click()
    btn = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_LoginButton"]').click()

    try:
      driver.find_element(By.XPATH, '//*[@id="contentbody"]/div/div[1]').click()
      # agree_btn = driver.find_element(By.XPATH, '//*[@id="ctl00_BodyContent_Agree"]')
      # agree_btn.click()
    except NoSuchElementException:
        pass
    # javaScript = "document.getElementById('ctl00_BodyContent_Agree').click();"
    # driver.execute_script(javaScript)

    t_id = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList"]/tbody/tr[2]/td[2]').text
    cash = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList_ctl02_lblCashBalance"]').text
    days_until_load = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList_ctl02_lblDaysUntilCashLoad"]').text
    last_txn = driver.find_element(
        By.XPATH, '//*[@id="ctl00_BodyContent_TerminalList"]/tbody/tr[2]/td[10]').text
    cash_balance = re.sub('\$', "", cash.replace(",", ""))

    post_one(t_id, int(float(cash_balance)), days_until_load, last_txn)
    email_one(t_id, int(float(cash_balance)), days_until_load, last_txn)
    results = get_all()
    for db_entry in results:
        print(db_entry)


    driver.quit()
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))

if __name__ == '__main__':
  main()