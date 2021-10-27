import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
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




## Register function, assumes already on register
# Tests if use is required to agree to TOS before signing up for Resume+
# Uses logout feature
def register():
    driver.find_element(By.ID,"fname").send_keys(user)
    driver.find_element(By.ID,"lname").send_keys(user)
    driver.find_element(By.ID,"username").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(user_pass)
    driver.find_element(By.ID,"confirm-password").send_keys(user_pass)
    driver.find_element(By.ID,"signup").click()
    if driver.current_url == "http://127.0.0.1:5000/register":
        print("Correctly ensures user accepts TOS")
        driver.find_element(By.ID, "newsletter").click()
        driver.find_element(By.ID, "signup").click()
    else:
        print("Incorrectly ensures user accepts TOS")
    # Logs us out and takes us back to register to test multiple accounts
    driver.get(flask_url + 'logout')
    driver.get(flask_url + 'register')

    #Try to sign up again with same acc
    driver.find_element(By.ID,"fname").send_keys(user)
    driver.find_element(By.ID,"lname").send_keys(user)
    driver.find_element(By.ID,"username").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(user_pass)
    driver.find_element(By.ID,"confirm-password").send_keys(user_pass)
    driver.find_element(By.ID,"signup").click()
    if driver.current_url == "http://127.0.0.1:5000/register":
        print("Correctly prevents multiple accounts")
    else:
        print("Does not ensure multiple accounts")

#sign up
#From landing page click signup button
driver.find_element(By.XPATH,"/html/body/header/div[1]/nav/div/a[2]/button").click()
register()

#sign in
#driver.find_element_by_id("signin-button").click()
#driver.find_element_by_id("username").send_keys(user)
#driver.find_element_by_id("Password").send_keys(user_pass)
#driver.find_element_by_id("signin").click()
