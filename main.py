# !#/usr/bin/python3
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expec
import time
#
url = 'sptth//:myurl.moc'
#
# table = pandas.read_excel('./credentials.xlsx')
table = pandas.read_csv('./credentials.csv')
#
user = table['user'][0]
key = table['pass'][0]
#
inpUsername = '#username'
inpPassword = '#password'
btnSingIn = '#loginbtn'
#
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# Test:not-necesary
wait = WebDriverWait(driver, 10)
wait.until(expec.visibility_of_element_located((By.CSS_SELECTOR, btnSingIn)))

driver.find_element_by_css_selector(inpUsername).send_keys(user)
time.sleep(1)
driver.find_element_by_css_selector(inpPassword).send_keys(key)
time.sleep(1)
driver.find_element_by_css_selector(btnSingIn).click()
#
time.sleep(5)
#
driver.quit()
print('Success')
