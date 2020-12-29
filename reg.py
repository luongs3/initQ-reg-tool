from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import sys

driver = webdriver.Chrome('/opt/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://initiativeq.com/invite/NRacuKyH4')
print("Sleep 5s ....")
time.sleep(5)

reserve = driver.find_element_by_link_text('Reserve your spot')
if reserve:
    reserve.click()
else:
    print("No Reserve your spot button detected!")
    sys.exit()

time.sleep(1)
first_form = driver.find_elements_by_xpath("//form")[1]
if first_form:
    print("first_form: ", first_form)
else:
    print("No first_form detected!")
    sys.exit()

input_name = first_form.find_elements_by_xpath(".//input")[0]
input_name.send_keys("Aramanda Lion")
input_email = first_form.find_elements_by_xpath(".//input")[1]
input_email.send_keys("aramandaLion@gmail.com")
input_psw = first_form.find_elements_by_xpath(".//input")[2]
input_psw.send_keys("luongQ1!")

sign_up_btn = first_form.find_element_by_xpath(".//button")
sign_up_btn.click()


