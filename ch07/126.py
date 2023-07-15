zip_code = input("우편번호: ")
if zip_code[:3] in ["010", "011", "012"]:
    print("Kangbuk-gu")
elif zip_code[:3] in ["013", "014", "015"]:
    print("Dobong-gu")
elif zip_code[:3] in ["016", "017", "018", "019"]:
    print("Nowon-gu")