# 네이버 로그인 자동화 
from selenium import webdriver

browser = webdriver.Chrome("/Users/hyeri/study/project/chromedriver")
browser.get("http://naver.com") 

browser.get("http://www.naver.com") 

# 로그인 배너 클릭
browser.find_element_by_class_name("link_login").click()

# 아이디, 비밀번호 입력

browser.find_element_by_id("id").send_keys("myid")
browser.find_element_by_id("pw").send_keys("mypw")

# 로그인 버튼 누르기

browser.find_element_by_id("log.login").click()

# 아이디 잘못입력했을 경우 
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# html 페이지 가져오기
print(browser.page_source)

