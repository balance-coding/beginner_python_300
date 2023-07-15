resident_number = input("input number: ")
gender = resident_number.split("-")[1]
location = int(gender[1:3])
if location in range(0, 9):
    print("seoul")
elif location in range(9, 13):
    print("Busan")
else:
    print("not seoul")