num_input = input("input: ")
num_print = int(num_input) - 20
if num_print < 0:
    print("print:", 0)
elif num_print > 255:
    print("print:", 255)
else:
    print("print:", num_print)
