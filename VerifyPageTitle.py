import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "D:\chromedriverwin32\chromedriver.exe")
driver.get("https://www.facebook.com/")
fbTitle = driver.title
expectedTitle = "Facebook – log in or sign up"
if(fbTitle == expectedTitle):
    print("Test Cased Passed")
else:
    print("Test Case failed")

driver.close()
