# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url='https://www.yogiyo.co.kr/mobile/#/414125/')

search_box = driver.find_element(by=By.CSS_SELECTOR, value='#content > div.restaurant-detail.row.ng-scope > '
                                                           'div.col-sm-8 > ul > li:nth-child(2) > a')
driver.implicitly_wait(20)
search_box.click()

review = driver.find_elements(by=By.XPATH, value='//*[@id="review"]/li/p')


for i in review:
    review_text = i.text
    print(review_text)

f = open(r"C:\Users\User\Documents\GitHub\Web-crawler\새파일.txt", 'w', encoding="utf-8")
for i in review:
    f.write(i.text)
    f.write("\n")
f.close()