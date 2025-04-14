import csv

# 저장할 데이터 (리스트의 리스트 형태)
data = [
    ['순위', '제목', '가수'],
    [1, '1노래', '1가수'],
    [2, '2노래', '2가수'],
    [3, '3노래', '3가수']
]

# CSV 파일 쓰기
# newline='' 옵션은 불필요한 빈 줄 생성을 방지합니다.
# encoding='utf-8' 또는 'utf-8-sig' (Excel에서 한글 깨짐 방지) 등을 지정할 수 있습니다.
try:
    with open('output.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)

        # 헤더 쓰기 (선택 사항)
        # writer.writerow(data[0])

        # 여러 행 쓰기
        writer.writerows(data)

        # 또는 한 행씩 쓰기
        # for row in data:
        #     writer.writerow(row)

    print("output.csv 파일이 성공적으로 생성되었습니다.")

except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")