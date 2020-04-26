from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)

url = "https://www.w3schools.com/default.asp"
driver.get(url)
my_list = []


def is_alert_present():
    try:
        driver.switch_to.alert
        return True
    except:
        return False

def assert_alert_present():
    if not is_alert_present():
        raise AssertionError("there is no alert here")
    else:
       print("there is an alert present!")
    return


def assert_current_title(expected_title):
    actual_title = driver.title
    if actual_title != expected_title:
        raise AssertionError("the title {} is different from {}.".format(actual_title,expected_title))
    else:
        #print("both titles match")
        y = "both titles match"
    return y


def assert_current_url(expected_url):
    actual_url = driver.current_url
    if actual_url != expected_url:
        raise AssertionError("the URL {} is different from {}.".format(actual_url,expected_url))
    else:
        #print("both URL's match")
        x = "both URL's match"
    return x


def my_main_method_test():
    main_page_title = driver.title
    return


driver.maximize_window()
time.sleep(1)
manage_consent_button = driver.find_element_by_css_selector("div#sncmp-banner-buttons")
time.sleep(1)
manage_consent_button.click()

agreed_and_proceed_button = driver.find_element_by_css_selector("#sncmp-popup-ok-button")
time.sleep(1)
agreed_and_proceed_button.click()
time.sleep(1)
driver.current_url

first_line = assert_current_title("W3Schools Online Web Tutorials")
second_line = assert_current_url("https://www.w3schools.com/default.asp")
my_list.append(first_line)
my_list.append(second_line)
f = open("CaLiN.txt","w+")
for i in my_list:
    f.write(i)
    f.write("\n")

f.close()

f = open("CaLiN.txt", "r")
for line in f:
    print(line)

driver.quit()
