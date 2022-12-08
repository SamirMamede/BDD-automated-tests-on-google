from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.google.com/')

element = driver.find_element(By.NAME, 'q')
element.click()
element.send_keys('google')
element.submit()

assert driver.title == "google - Pesquisa Google"

driver.close()

