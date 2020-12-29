from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php')
print("Sleep 5s ...")
time.sleep(5)
reserve = driver.find_element_by_link_text('⤴️ Try again')
if reserve:
    reserve.click()
else:
    print("No Try again button detected!")



