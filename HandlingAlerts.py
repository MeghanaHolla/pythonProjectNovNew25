import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element_by_link_text("JavaScript Alerts").click()

driver.find_element_by_css_selector("#content > div > ul > li:nth-child(1) > button").click()

time.sleep(5)
driver.switch_to.alert.accept()