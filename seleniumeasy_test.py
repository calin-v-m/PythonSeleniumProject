from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/")


def navigate_to_subscribe():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    subscribe_button = driver.find_element_by_css_selector("#mc-embedded-subscribe")
    subscribe_button.click()
    return


def get_num_of_windows():
    windows_list = driver.window_handles
    # number_of_win = len(windows_list)
    # print(str(number_of_win) + " handles available")
    return windows_list


def assert_on_window_title(title):
    actual_title = "https://seleniumeasy.us15.list-manage.com/subscribe/post?u=a5d2efe08ad93a8b91b578279&id=5d70235043"
    if title != actual_title:
        raise Exception(" the two titles do not match")
    else:
        print("this is the correct one and that is: {}".format(title))
    return


def fill_fields_and_submit_info():
    email_text_field = driver.find_element_by_css_selector("#MERGE0")
    email_text_field.send_keys("myEmailCalin@gmail.com")
    time.sleep(1)
    fName = driver.find_element_by_css_selector("#MERGE1")
    fName.send_keys("CalinTester")
    time.sleep(1)
    lName = driver.find_element_by_css_selector("#MERGE2")
    lName.send_keys("CalinLastName")
    time.sleep(1)
    return


def send_info_for_subscribe():
    button = driver.find_element_by_css_selector("div .formEmailButton")
    time.sleep(1)
    button.click()
    return


def assert_if_we_are_human():
    humanity_text = driver.find_element_by_css_selector("div #templateBody h2").text
    if humanity_text != "Confirm Humanity":
        raise Exception("the page is not the one we expected! ")
    else:
        #print("we are oin the right page :)")
        x = "we are on the right page :)"
    return x


def write_in_text_file():
    f = open("output_text_file.txt","w+")
    f.write(my_text)
    f.close()
    return


def read_from_text_file_and_print():
    f = open("output_text_file.txt", "r")
    for line in f:
        print(line)
    return


navigate_to_subscribe()
my_list = get_num_of_windows()
# print(my_list)
driver.switch_to.window(my_list[1])
assert_on_window_title(driver.current_url)
fill_fields_and_submit_info()
send_info_for_subscribe()
my_text = assert_if_we_are_human()
driver.quit()
write_in_text_file()
read_from_text_file_and_print()




#
# options = webdriver.ChromeOptions()
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--incognito")
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
#
# driver.get("https://www.pluralsight.com/")
#
# driver.close()
