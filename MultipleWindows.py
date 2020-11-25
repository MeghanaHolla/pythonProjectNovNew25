from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "D:\Training\Drivers\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element_by_link_text("Multiple Windows").click()
driver.find_element_by_link_text("Click Here").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])

actualText = driver.find_element_by_css_selector("body > div > h3").text
if (actualText == "New Window"):
    print("Pass")
else:
    print("Fail")

#driver.quit()
driver.close()

driver.switch_to.window(windows[0])
driver.close()