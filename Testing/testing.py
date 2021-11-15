import selenium
from selenium import webdriver
from seleniumrequests import Chrome
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
import time
#Test Navigation
unregistered_pages = {"/about","/support","/","/login", "/register"}
registered_pages = {"/home_page", "/account/profile", "/account/settings"}
flask_url = "http://127.0.0.1:5000"
user = "testing_name"
email = "testing@ResumePlus.com"
user_pass = "testing_pass"
#Start the web browser in chrome
driver = webdriver.Chrome(options=options)
#Load the default page
driver.get(flask_url)

#Click the sign in button


## Function to logg into resume ResumePlus
def login():
    driver.post(flask_url + "/login", data={"username" : user, "password" : user_pass})
    if not driver.current_url == flask_url + "/home_page":
        print("Error: Unable to login")

## Register function, assumes already on register
# Tests if use is required to agree to TOS before signing up for Resume+
# Uses logout feature
def register():
    driver.get(flask_url + '/register')
    driver.find_element(By.ID,"fname").send_keys(user)
    driver.find_element(By.ID,"lname").send_keys(user)
    driver.find_element(By.ID,"username").send_keys(user)
    driver.find_element(By.ID,"email").send_keys(email)
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
    driver.get(flask_url + '/logout')
    driver.get(flask_url + '/register')

    #Try to sign up again with same acc
    driver.find_element(By.ID,"fname").send_keys(user)
    driver.find_element(By.ID,"lname").send_keys(user)
    driver.find_element(By.ID,"username").send_keys(user)
    driver.find_element(By.ID,"email").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(user_pass)
    driver.find_element(By.ID,"confirm-password").send_keys(user_pass)
    driver.find_element(By.ID,"signup").click()
    if driver.current_url == "http://127.0.0.1:5000/register":
        print("Correctly prevents multiple accounts")
    else:
        print("Does not ensure multiple accounts")

# Method to test navigation to all pages while logged out
def test_nav_out():
    for i in unregistered_pages:
        driver.get(flask_url+i)
        if not driver.current_url == str(flask_url+i):
            print("ERROR : Unable to navigate to " + flask_url + i)
    for i in registered_pages:
        driver.get(flask_url+i)
        if driver.current_url == str(flask_url+i):
            print("ERROR: able to navigate to " + flask_url + i)

def test_nav_in():
    register()


#sign up
#From landing page click signup button
driver.find_element(By.XPATH,"/html/body/header/div[1]/nav/div/a[2]/button").click()
test_nav_out()
register()
login()


#sign in
#driver.find_element_by_id("signin-button").click()
#driver.find_element_by_id("username").send_keys(user)
#driver.find_element_by_id("Password").send_keys(user_pass)
#driver.find_element_by_id("signin").click()
