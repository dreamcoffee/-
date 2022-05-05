# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url='https://www.yogiyo.co.kr/mobile/#/414125/')

driver.implicitly_wait(10)
time.sleep(5)
search_box = driver.find_element(by=By.CSS_SELECTOR, value='#content > div.restaurant-detail.row.ng-scope > '
                                                           'div.col-sm-8 > ul > li:nth-child(2) > a')
search_box.click()

# 리뷰 데이터를 찾습니다.
review = driver.find_elements(by=By.XPATH, value='//*[@id="review"]/li/p')

for i in review:
    review_text = i.text
    print(review_text)

a = 1
f = open(r"C:\Users\User\Documents\GitHub\Web-crawler\데이터처리\reviewData.csv", 'w', encoding="utf-8-sig", newline='')
for i in review:
    wr = csv.writer(f)
    wr.writerow([a, i.text])
    a += 1

f.close()
driver.quit()
