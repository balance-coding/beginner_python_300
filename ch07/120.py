fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input_fruit = input("favorite fruit: ")
if input_fruit in fruit.values():
    print("answer!")
else:
    print("wrong!")