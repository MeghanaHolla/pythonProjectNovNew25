from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element_by_link_text("Checkboxes").click()
checkbox_selected = driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(3)").is_selected()
if checkbox_selected == True:
    driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(3)").click()