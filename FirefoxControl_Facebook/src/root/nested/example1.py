from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")

username = driver.find_element_by_name("email")
username.clear()
username.send_keys("test@test.com")

password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("password")

loginButton = driver.find_element_by_id("loginbutton")
loginButton = loginButton.find_element_by_tag_name("input")
loginButton.click()