import selenium
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
import time

flask_url = " http://127.0.0.1:5000/"
user = "testing_name"
email = "testing@ResumePlus.com"
user_pass = "testing_pass"
#Start the web browser in chrome
driver = webdriver.Chrome(options=options)
#Load the default page
driver.get(flask_url)

#Click the sign in button

#Wait for page to load
time.sleep(3)

#sign up
driver.find_element_by_xpath("/html/body/header/div[1]/nav/ul/div/a[2]/button").click()
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("lname").send_keys(user)
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("password").send_keys(user_pass)
driver.find_element_by_id("confirm-password").send_keys(user_pass)
driver.find_element_by_id("signup").click()
if driver.current_url == "http://127.0.0.1:5000/registerV2":
    print("Correctly ensures user accepts TOS")
    driver.find_element_by_id("newsletter").click()
    driver.find_element_by_id("signup").click()
else:
    print("Incorrectly ensures user accepts TOS")



#sign in
driver.find_element_by_id("signin-button").click()
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("Password").send_keys(user_pass)
driver.find_element_by_id("signin").click()
