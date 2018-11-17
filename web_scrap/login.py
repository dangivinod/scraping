from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import csv
count = 0

def login_user(driver):
    import pdb; pdb.set_trace()
    time.sleep(3)
    username = driver.find_element_by_xpath('//*[@id="Site"]/ngb-modal-window/div/div/ghs-authentication-wizard-modal/div/ghs-authentication-wizard/div/div/div/ghs-sign-in/div/form/div[1]/div/span/div/input')
    time.sleep(2)
    password = driver.find_element_by_xpath('//*[@id="Site"]/ngb-modal-window/div/div/ghs-authentication-wizard-modal/div/ghs-authentication-wizard/div/div/div/ghs-sign-in/div/form/div[2]/div[1]/div/input')
    time.sleep(2)
    submit = driver.find_element_by_xpath('//*[@id="Site"]/ngb-modal-window/div/div/ghs-authentication-wizard-modal/div/ghs-authentication-wizard/div/div/div/ghs-sign-in/div/form/div[3]/div/ghs-sign-in-btn/button')
    time.sleep(2)
    username.clear()
    username.send_keys('username@email.com')
    password.clear()
    password.send_keys('password')
    submit.send_keys(Keys.RETURN)
    time.sleep(2)
    if 'vinod' in driver.page_source:
        # import pdb; pdb.set_trace()
        print("***************************************")
        # addressInput-textInput
        address = driver.find_element_by_xpath('//*[@id="ghs-start-order-new-address-input"]/div/div/div/input')
        time.sleep(2)
        submit = driver.find_element_by_xpath('//*[@id="ghs-startOrder-searchBtn"]')
        time.sleep(2)
        address.send_keys('Indore Ct, Middle Creek, NC, 27526')
        time.sleep(2)
        submit.send_keys(Keys.RETURN)
        time.sleep(2)
        
        open_now = driver.find_element_by_xpath('//*[@id="ghs-search-results-container"]/div/div[2]/div/div/ghs-search-results/div/div/div[1]/div/div/div[1]/ghs-search-results-bread-crumbs/div/div/ul/li')
        time.sleep(2)
        open_now.click()
        print("Browse food near you name list")
        items = driver.find_elements_by_class_name('ghs-cuisineRibbon-value')
        time.sleep(2)
        for item in items:
            print(item.text)
        print("Browse food near you image source")
        time.sleep(2)
        items = driver.find_elements_by_class_name('cuisineRibbon-cuisine-image')
        time.sleep(2)
        for img in items:
            print(img.get_attribute('src'))
        print("***************************************")
        time.sleep(2)
        items = driver.find_elements_by_class_name('restaurantCard-search')
        time.sleep(2)
        print("Restorent Name || detais || Rating || Image ")
        for item in items:
            print(item.find_elements_by_class_name('restaurant-name')[0].text +' || '+ item.find_elements_by_class_name('restaurantCard-search-cuisines')[0].text +' || '+item.find_elements_by_class_name('starRating-text--xs')[0].text +' || '+item.find_elements_by_tag_name('img')[0].get_attribute('src'), sep=" || ")
    else:
        return False

driver = webdriver.Firefox(executable_path=r'E:\scraping_project\geckodriver.exe')
driver.get("https://www.grubhub.com/")
login_click = driver.find_element_by_xpath('//*[@id="Site"]/ghs-site-container/div/ghs-main-nav/div/ghs-preact[1]/ghs-main-nav-profile/div/div/button')
# login_click.text
login_click.click()
time.sleep(2)
user_log = login_user(driver)
print(user_log)
while user_log == False:
    time.sleep(2)
    print(user_log)
    user_log = login_user(driver)
    time.sleep(2)

