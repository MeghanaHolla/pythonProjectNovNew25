import pytest
from selenium import webdriver

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    driver = webdriver.Chrome(executable_path="D:\\Training\\Drivers\\chromedriver.exe")
    driver.get("https://www.monster.com")
    driver.minimize_window()
    driver.implicitly_wait(30)

    yield
    driver.close()

#New Code insert to Test PULL Request
def test_verify_page_title(init_driver):
    actual_title = driver.title
    assert actual_title == "Job Vacancy - Latest Job Openings - Job Search Online - Monster India"

def test_verify_test(init_driver):
    actual_Text = driver.find_element_by_css_selector("#user-signup-actions > div:nth-child(1) > div > h2").text
    assert actual_Text == "NEW TO MONSTER?"

def test_verify_loginBtn_visibility(init_driver):
    loginBtn_visible = driver.find_element_by_id("seekerLoginBtn").is_displayed()
    assert True == loginBtn_visible

def test_verify_searBtn_enabled(init_driver):
    searchBtn_enabled = driver.find_element_by_css_selector("#searchForm > div > div.col-xl-2.col-lg-3.col-sm-2.col-xxs-12.fl.no-padding > input").is_enabled()
    assert True == searchBtn_enabled