from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element_by_id("u_0_2").click()
monthDD = driver.find_element_by_id("month")
dd = Select(monthDD)
dd.select_by_value("9")
#dd.select_by_visible_text("Jan")
#dd.select_by_index(3)
# driver.switch_to.frame("classFrame")
# driver.find_element_by_link_text("HELP").click()
#
# driver.switch_to.default_content()

# driver.switch_to.frame("packageFrame")
# driver.find_element_by_link_text("Actions").click()