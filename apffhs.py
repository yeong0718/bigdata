import requests
from bs4 import BeautifulSoup
import pandas as pd

# 멜론 차트 페이지 URL
url = "https://www.melon.com/chart/index.htm"

# HTTP 헤더 설정 (User-Agent 필요)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# 페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 순위, 제목, 가수 가져오기
songs = soup.select("tr.lst50, tr.lst100")  # 1~100위까지 가져오기
data = []

for song in songs:
    rank = song.select_one("span.rank").text  # 순위
    title = song.select_one("div.ellipsis.rank01 a").text  # 노래 제목
    artist = song.select_one("div.ellipsis.rank02 a").text  # 가수 이름
    data.append([rank, title, artist])

# DataFrame으로 정리
df = pd.DataFrame(data, columns=["순위", "제목", "가수"])
print(df)

# CSV 파일로 저장 가능
df.to_csv("melon_top100.csv", index=False, encoding="utf-8-sig")

