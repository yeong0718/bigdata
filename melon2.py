print("==================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("==================")

# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")

# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
    #수집한 데이터를 출력합니다
    for song in range(100):
        print(f"{songs[i][0]}, {songs[i][1]} - {songs[i][2]}")
#else:
#    print("1이 아닙니다.")
# 만약에 2을 입력하면
elif n == "2":
    print("멜론 50")
# 멜론 50 출력
elif n == "3":
    print("멜론 10")
elif n == "4":
    print("AI 추천 노래")
     # 멜론 차트 100 중에서 노래 한곡 추천 해주는 서비스 만들기
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.")
    
elif n == "5":
    print("가수 이름 검색")
# ...
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 나와야함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
else:
    print("1~5까지 입력하세요")