from selenium import webdriver

driver = webdriver.Chrome(executable_path = "D:\chromedriverwin32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element_by_id("email").send_keys("ironman3842770@hotmail.com")

driver.find_element_by_id("pass").send_keys("pass12343")

driver.find_element_by_name('login').click()

actualErrMsg = driver.find_element_by_css_selector("#email_container > div._9ay7").text
expectedErrMsg = "The email address that you've entered doesn't match any account. Sign up for an account."

if (actualErrMsg == expectedErrMsg):
    print("Test Case Passed")
else:
    print("Test Case Failed")

driver.close()