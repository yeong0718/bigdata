import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'

# 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트 수집
for entry in soup.select('tr.lst50, tr.lst100'):
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 메뉴 출력
print("==================")
print("1. 멜론 TOP 100")
print("2. 멜론 TOP 50")
print("3. 멜론 TOP 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("==================")

# 메뉴 선택
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")

# 메뉴 1: 멜론 100
if n == "1":
    print("멜론 100")
    for i in range(100):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 메뉴 2: 멜론 50
elif n == "2":
    print("멜론 50")
    for i in range(50):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 메뉴 3: 멜론 10
elif n == "3":
    print("멜론 10")
    for i in range(10):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 메뉴 4: AI 추천 노래
elif n == "4":
    print("AI 추천 노래")
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.")

# 메뉴 5: 가수 이름 검색
elif n == "5":
    print("가수 이름 검색")
    search = input("검색할 가수 이름을 입력하세요: ")
    for i in range(len(songs)):
        if search.lower() in songs[i][2].lower():
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 그 외 숫자
else:
    print("1~5까지 입력하세요.")
