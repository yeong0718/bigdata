import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

songs = []

# 차트에서 제목과 가수 정보를 가져옵니다.
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

# 사용자 입력 받기
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은: {n}")

# 메뉴 1: 멜론 100
if n == "1":
    print("\n 멜론 TOP 100")
    for i in range(len(songs)):
        print(f"{songs[i][0]}위: {songs[i][1]} - {songs[i][2]}")

# 메뉴 2: 멜론 50
elif n == "2":
    print("\n 멜론 TOP 50")
    for i in range(min(50, len(songs))):
        print(f"{songs[i][0]}위: {songs[i][1]} - {songs[i][2]}")

# 메뉴 3: 멜론 10
elif n == "3":
    print("\n 멜론 TOP 10")
    for i in range(min(10, len(songs))):
        print(f"{songs[i][0]}위: {songs[i][1]} - {songs[i][2]}")

# 메뉴 4: AI 추천 노래
elif n == "4":
    print("\n AI 추천 노래")
    ai_song = random.choice(songs)
    print(f"오늘의 추천곡은  {ai_song[1]} - {ai_song[2]} 입니다.")

# 메뉴 5: 가수 이름 검색
elif n == "5":
    search_name = input("가수 이름을 입력하세요: ")
    print(f"\n '{search_name}'의 노래 목록:")
    found = False
    for song in songs:
        if search_name.lower() in song[2].lower():
            print(f"{song[0]}위: {song[1]} - {song[2]}")
            found = True
    if not found:
        print("해당 가수의 노래가 차트에 없습니다.")

# 그 외 입력
else:
    print(" 1부터 5 사이의 숫자만 입력해주세요.")
