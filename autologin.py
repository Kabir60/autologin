from pprint import pprint

from selenium import webdriver
from getpass import getpass

username = "your user name"
password = "your password"


driver = webdriver.Chrome(
    "C:\\Users\\kabir\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("website link")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name("login")
login_button.submit()



