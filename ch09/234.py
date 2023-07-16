def pickup_even(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)

    return even

print(pickup_even([3, 4, 5, 6, 7, 8]))