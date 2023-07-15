resident_number = input("resident number: ")
front = resident_number.split("-")[0]
back = resident_number.split("-")[1]
front_mul = "234567"
back_mul = "892345"
sum = 0
for i in range(6):
    sum += int(front[i])*int(front_mul[i]) + int(back[i])*int(back_mul[i])

result1 = sum % 11
result2 = 11 - result1
if result2 == back[6]:
    print("OK")
else:
    print("WRONG")

