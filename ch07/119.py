fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input_season = input("favorite season: ")
if input_season in fruit.keys():
    print("answer!")
else:
    print("wrong!")