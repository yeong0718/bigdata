from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Chrome 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 창 없이 실행 (필요하면 주석 처리)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Chrome WebDriver 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 팬카페 이동
url = "https://cafe.naver.com/youngcu"
driver.get(url)

# 잠시 대기 (로딩될 때까지)
time.sleep(3)

# "인기글" 이동 (인기글 URL이 다를 수도 있음, 직접 확인 필요)
popular_posts = driver.find_elements(By.CSS_SELECTOR, ".article-board a.article")
titles = []

for post in popular_posts[:10]:  # 상위 10개만 가져오기
    titles.append(post.text)

# 크롬 드라이버 종료
driver.quit()

# 결과 출력
df = pd.DataFrame(titles, columns=["인기글 제목"])
print(df)

# CSV 파일로 저장 가능
df.to_csv("fan_cafe_popular_posts.csv", index=False, encoding="utf-8-sig")
