my_list = [100, 200, 400, 800]

for i in range(len(my_list) - 1):
    sub = my_list[i+1]-my_list[i]
    print(sub)