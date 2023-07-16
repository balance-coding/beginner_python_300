def printmxn(data, num):
    check = int(len(data)/num)
    for i in range(check+1):
        print(data[i*num:i*num+num])

printmxn("아이엠어보이유알어걸", 3)
