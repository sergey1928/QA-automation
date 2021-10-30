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
# login = driver.find_element_by_id("username")
# login.send_keys("reg_email@mail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("oxymOron19@(!LBHUN")
#
# login_btn = driver.find_element_by_xpath("//input[@name='login']")
# login_btn.click()
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# book = driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']")
# book.click()
# driver.implicitly_wait(5)
#
# element = driver.find_element_by_css_selector("div>h1")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"


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
# login = driver.find_element_by_id("username")
# login.send_keys("reg_email@mail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("oxymOron19@(!LBHUN")
#
# login_btn = driver.find_element_by_xpath("//input[@name='login']")
# login_btn.click()
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# html = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product-category/html/']")
# html.click()
#
# from selenium.webdriver.common.by import By
# count = driver.find_elements(By.XPATH, "//img[@width='300']")
# if len(count) == 3:
#     print("3 товара")
# else:
#     print("Ошибка. " + str(len(count)))

    #сортировка товаров
#
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
# login = driver.find_element_by_id("username")
# login.send_keys("reg_email@mail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("oxymOron19@(!LBHUN")
#
# login_btn = driver.find_element_by_xpath("//input[@name='login']")
# login_btn.click()
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# from selenium.webdriver.support.select import Select
# element = driver.find_element_by_xpath("//select[@class='orderby']")
# select = Select(element)
# select.select_by_value("menu_order")
# driver.implicitly_wait(5)
#
# element = driver.find_element_by_xpath("//select[@class='orderby']")
# select = Select(element)
# select.select_by_value("price-desc")
# driver.implicitly_wait(5)
#
#
# element = driver.find_element_by_xpath("//select[@class='orderby']")
# element_get_text = element.text
# assert element_get_text == ("Sort by price: high to low")
# driver.implicitly_wait(5)

#отображение/скидка

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
# login = driver.find_element_by_id("username")
# login.send_keys("reg_email@mail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("oxymOron19@(!LBHUN")
#
# login_btn = driver.find_element_by_xpath("//input[@name='login']")
# login_btn.click()
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# book =  driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']")
# book.click()
# driver.implicitly_wait(5)
#
# element = driver.find_element_by_xpath("//span[text()='600.00']")
# element_get_text = element.text
# assert element_get_text =='₹600.00'
# driver.implicitly_wait(5)
#
# element_2 =driver.find_element_by_xpath("//span[text()='450.00']")
# element_get_text = element_2.text
# assert element_get_text =='₹450.00'
# driver.implicitly_wait(5)
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
#
# book_img = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']")) )
# book_img.click()
#
# close_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "div>a.pp_close")) )
# close_btn.click()

# Shop: проверка цены в корзине

# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# add_basket = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']")
# add_basket.click()
# driver.implicitly_wait(5)
#
# element = driver.find_element_by_xpath("//span[@class='cartcontents']")
# element_get_text = element.text
# assert "Item" in element_get_text
# driver.implicitly_wait(5)
#
# element_2 = driver.find_element_by_xpath("//span[@class='amount']")
# element_get_text = element_2.text
# assert "₹" in element_get_text
# driver.implicitly_wait(5)
#
# basket_btn = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/basket/']")
# basket_btn.click()
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# Subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal']"), "180.00"))
#
# Total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>span"), "189.00"))
#
# # shop:покупка товара
#
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# driver.implicitly_wait(5)
#
# shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
# shop.click()
# driver.implicitly_wait(5)
#
# driver.execute_script("window.scrollBy(0, 300);")
#
# add_basket = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']")
# add_basket.click()
#
# basket_btn = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/basket/']")
# basket_btn.click()
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# Proceed_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@class='checkout-button button alt wc-forward']")))
# Proceed_btn.click()
#
# first_name = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.XPATH,"//label[@for='billing_first_name']"),"First Name" ))
#
# first_name_btn = driver.find_element_by_xpath("//input[@name='billing_first_name']")
# first_name_btn.send_keys("Sergei")
#
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Ivanov")
#
# email = driver.find_element_by_id("billing_email")
# email.send_keys("Mail@gmail.com")
#
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("+79985554411")
#
# selector = driver.find_element_by_id("s2id_billing_country")
# selector.click()
#
# select_input = driver.find_element_by_id("s2id_autogen1_search")
# select_input.send_keys("Amer")
#
# country = driver.find_element_by_id("select2-result-label-481")
# country.click()
#
# adress = driver.find_element_by_id("billing_address_1")
# adress.send_keys("SPB Dvorcovaya 1")
#
# town = driver.find_element_by_id("billing_city")
# town.send_keys("SPB")
#
# state = driver.find_element_by_id("billing_state")
# state.send_keys("American Samua")
#
# post =  driver.find_element_by_id("billing_postcode")
# post.send_keys("111111")
#
# driver.execute_script("window.scrollBy(0, 600);")
#
# value = driver.find_element_by_xpath("//input[@value='cheque']")
# value.click()
# driver.implicitly_wait(5)
#
# order = driver.find_element_by_id("place_order")
# order.click()
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# final = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.XPATH,"//p[@class='woocommerce-thankyou-order-received']"),"Thank you. Your order has been received" ))
#
# payment_method  = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.XPATH,"//strong[text()='Check Payments']"),"Check Payments"))

# работа в корзине

import time
from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)

shop = driver.find_element_by_xpath("//li[@id='menu-item-40']")
shop.click()
driver.implicitly_wait(5)

add_basket = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']")
add_basket.click()
driver.implicitly_wait(5)

add_js = driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=180']")
add_js.click()

basket_btn = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/basket/']")
basket_btn.click()

del_book = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/basket/?remove_item=045117b0e0a11a242b9765e79cbf113f&_wpnonce=bccc494fc5']")
time.sleep(3)
del_book.click()

undo = driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/basket/?undo_item=4c5bde74a8f110656874902f07378009&_wpnonce=bccc494fc5']")
undo.click()

Qnt = driver.find_element_by_xpath("//input[@type='number']")
Qnt.clear()

Qnt = driver.find_element_by_xpath("//input[@type='number']")
Qnt.send_keys("3")

update_basket = driver.find_element_by_css_selector("td>input.button")
update_basket.click()

Qnt = driver.find_element_by_xpath("//input[@type='number']")
Qnt_get_text = Qnt.text
assert Qnt_get_text == "3"

apply = driver.find_element_by_name("[name='apply_coupon']")
apply.click()

mes = driver.find_element_by_xpath("//ul[@class='woocommerce-error']")
mes_get_text = mes.text
assert  mes_get_text == "Please enter a coupon code."