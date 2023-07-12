time = input("now: ")
minute = time.split(":")
if minute[1] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")