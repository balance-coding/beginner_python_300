warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
input_investment = input("input investment: ")
if input_investment in warn_investment_list:
    print("It is one of warn investment list.")
else:
    print("It isn't one of warn investment list.")
