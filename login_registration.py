# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
#
# my_acc = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/my-account/']")
# my_acc.click()
#
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("reg_email@mail.com")
#
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("oxymOron19@(!LBHUN")
#
#
# reg_button = driver.find_element_by_xpath("//input[@name='register']")
# reg_button.click()


#registration
import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

my_acc = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/my-account/']")
my_acc.click()

login = driver.find_element_by_id("username")
login.send_keys("reg_email@mail.com")

password = driver.find_element_by_id("password")
password.send_keys("oxymOron19@(!LBHUN")

login_btn = driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()

driver.implicitly_wait(5)

element = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/my-account/customer-logout/']") 	# нашли элемент по составному селектору
element_get_text = element.text
assert "Logout" in element_get_text

