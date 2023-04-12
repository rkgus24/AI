from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def get_title_of_post(driver, url):
    title_list = []
    driver.get(url)
    posts = driver.find_elements_by_class_name('ub-content')

    for i in range(0, len(posts)):
        if posts[i].find_element_by_class_name('gall_date').text == "04/12":
            post_title = posts[i].find_element_by_tag_name('a').text
            title_list.append(post_title)
    return title_list

def isTodayPostOnpage(driver, url, date):
    driver.get(url)
    posts = driver.find_elements_by_class_name('gall_date')

    for i in range(0, len(posts)):
        if posts[i].text == date:
            return True
    return False

def main():
    driver = webdriver.Chrome('./chromedriver')
    url = 'http://gall.dcinside.com/board/lists?id=cat&page='
    page_Number = 1
    while True:
        if isTodayPostOnpage(driver, url+str(page_Number), "04/12"):    
            print(get_title_of_post(driver, url+str(page_Number)))
            page_Number+=1
        else:
            break

    # 5초 후에 자동으로 웹드라이버를 종료
    time.sleep(True)
    driver.quit()

if __name__=="__main__":
    main()
