import requests
from bs4 import BeautifulSoup
import pandas as pd

# 네이버 뉴스 검색 URL (추영우 키워드 포함)
query = "추영우"
url = f"https://search.naver.com/search.naver?where=news&query={query}"

# HTTP 요청 헤더 (403 오류 방지)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# 페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 뉴스 기사 정보 가져오기
news_list = soup.select("ul.list_news > li")  # 네이버 뉴스 리스트

# 뉴스 데이터 저장
data = []
for news in news_list[:10]:  # 상위 10개 기사만 가져오기
    title_tag = news.select_one("a.news_tit")  # 기사 제목
    if title_tag:
        title = title_tag.text.strip()
        link = title_tag["href"]  # 기사 링크
        press = news.select_one("a.info.press").text.strip()  # 언론사
        
        data.append([title, press, link])

# DataFrame으로 정리
df = pd.DataFrame(data, columns=["제목", "언론사", "링크"])
print(df)

# CSV 파일로 저장 가능
df.to_csv("chu_young_woo_news.csv", index=False, encoding="utf-8-sig")
