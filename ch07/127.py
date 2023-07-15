resident_number = input("input number: ")
gender = resident_number.split("-")[1]
if gender[0] in ["1", "3"]:
    print("man")
elif gender[0] in ["2", "4"]:
    print("woman")