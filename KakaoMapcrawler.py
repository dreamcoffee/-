# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver', options=options)


def main():
    global driver
    Enter = input("원하는 검색어를 입력해주세요 : ")
    driver.implicitly_wait(5)
    driver.get(url='https://map.kakao.com/')
    search(Enter)
#    driver.quit()


def file():
    f = open(r"C:\Users\User\Documents\GitHub\Web-crawler\데이터처리\reviewData2.csv", 'w', encoding="utf-8-sig", newline='')
    wr = csv.writer(f)
    wr.writerow(["이름", "주소", "전화번호", "리뷰"])


def search(Enter):
    global driver
    time.sleep(1)  # 추가적인 로딩 방지를 위해 추가적으로 1초 대기합니다.

    # 검색을 위한 구문입니다.
    search_box = driver.find_element(by=By.CSS_SELECTOR, value='#search\.keyword\.query')
    search_box.send_keys(Enter)
    search_box.send_keys(Keys.ENTER)

    time.sleep(1)
    moreview = driver.find_element(by=By.ID, value="info.search.place.more")
    moreview.send_keys(Keys.ENTER)

    page = driver.find_element(by=By.ID, value='info.search.page.no1')
    page.send_keys(Keys.ENTER)

    time.sleep(1)
    view_details = driver.find_element(by=By.XPATH, value='//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]')
    view_details.send_keys(Keys.ENTER)

    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.implicitly_wait(5)
    time.sleep(1)
    review_page = driver.find_elements(by=By.CLASS_NAME, value="link_page")
    review_page_num = len(review_page)
    print(review_page_num)


#def review_crawling():
#    global driver
    # 리뷰 데이터를 수집합니다.
#    review = driver.find_elements(by=By.CSS_SELECTOR, value='txt_comment > span')
#    print(review)


if __name__ == "__main__":
    main()





