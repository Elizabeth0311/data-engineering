from selenium import webdriver

browser = webdriver.Chrome("/Users/hyeri/study/project/chromedriver") 
browser.get("http://naver.com") 

# element 객체 생성 / html 클래스 이름 가져오기
elem = browser.find_element_by_class_name("link_login")

# 검색창 id 값 가져오기
elem = browser.find_element_by_id("query")

# 값 입력시 필요한 모듈 import
from selenium.webdriver.common.keys import Keys

# 검색어 넣기
elem.send_keys("파이썬")
# 검색 
elem.send_keys(Keys.ENTER)

# 태그로 정보 가져오기
elem = browser.find_element_by_tag_name("a")

# 해당 태그의 모든 정보 가져오기
elem = browser.find_elements_by_tag_name("a")

# 뒤로가기
browser.back()
# 앞으로가기 
browser.forward()
# 브라우저 탭 닫기
browser.close()
# 브라우저 종료
browser.quit()