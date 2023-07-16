def make_list(data):
    list = []
    for i in range(len(data)):
        list.append(data[i])

    return list

print(make_list("abcd"))

def make_list2(data):
    return list(data)

print(make_list2("abcd"))