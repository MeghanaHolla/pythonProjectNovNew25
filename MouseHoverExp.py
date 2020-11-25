from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.implicitly_wait(20)
driver.maximize_window()

el = driver.find_element_by_id("nav-link-accountList")
hover = ActionChains(driver)
hover.move_to_element(el).perform()

driver.find_element_by_id("nav_prefetch_yourorders").click()