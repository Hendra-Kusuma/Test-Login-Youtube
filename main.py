# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc # Using undetected_chromedriver to bypass google alert "this browser or app not
# be secure"
import time

driver = uc.Chrome(use_subprocess=True)

driver.get("https://accounts.google.com/ServiceLogin/identifier?service=youtube&uilel=3&passive=true&continue=https"
           "%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps"
           "%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

phone_number = "xxx" #you can use your phone number in connected to google account
password = "xxx" #you can use your password in connected to google account


def login_test():
    element = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    element.send_keys(phone_number)
    time.sleep(5)
    element.send_keys(Keys.RETURN)
    time.sleep(5)
    element = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    time.sleep(10)  # waiting 10 minutes after executed login form submission
    driver.close()  # chrome will be automatically closed after 3 minutes


if __name__ == '__main__':
    login_test()

# after this enter phone number and password, next step, Google have security 2 step and must be solved by human, so its cannot automation for all step