import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0, 600);")
selenium_btn= driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product/selenium-ruby/']")
selenium_btn.click()

driver.implicitly_wait(5)
reviews_btn = driver.find_element_by_xpath("//a[@href='#tab-reviews']")
reviews_btn.click()

stars = driver.find_element_by_css_selector("span>.star-5")
stars.click()

comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Sergei")

email = driver.find_element_by_id("email")
email.send_keys("mail@mail.com")

submit = driver.find_element_by_id("submit")
submit.click()
# driver.quit()