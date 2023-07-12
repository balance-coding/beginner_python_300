input_data = input("input: ")
num, currency = input_data.split()
data = {"달러":1167, "엔":1.096, "유로":1268, "위안":171}
if currency in data.keys():
    print(float(num)*data[currency], "원")