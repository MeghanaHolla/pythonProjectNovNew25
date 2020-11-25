import pytest
from selenium import webdriver

@pytest.mark.FBTest
def test_verify_FB_title():
    driver = webdriver.Chrome(executable_path="D:\\Training\\Drivers\\chromedriver.exe")
    driver.get("https://facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actualTitle = driver.title
    assert actualTitle == "Facebook – log in or sign up"
    driver.close()

@pytest.mark.GoogleTest
def test_verify_Google_title():
    driver = webdriver.Chrome(executable_path="D:\\Training\\Drivers\\chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actualTitle = driver.title
    assert actualTitle == "Google"
    driver.close()