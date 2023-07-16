def print_5xn(data):
    check = int(len(data)/5)
    for i in range(check+1):
        print(data[i * 5:i * 5 + 5])

print_5xn("아이엠어보이유알어걸")
