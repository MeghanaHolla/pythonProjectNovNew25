from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.implicitly_wait(20)

driver.find_element_by_link_text("Dynamic Loading").click()
driver.find_element_by_partial_link_text("Example 1").click()
driver.back()
driver.forward()
driver.refresh()

driver.find_element_by_css_selector("#start > button").click()
wait = WebDriverWait(driver,20,poll_frequency=3,ignored_exceptions = [ElementNotVisibleException])

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#finish > h4")))
actualText = driver.find_element_by_css_selector("#finish > h4").text
if (actualText == "Hello World!"):
    print("Test Case Passed")
else:
    print("Test case Failed")

