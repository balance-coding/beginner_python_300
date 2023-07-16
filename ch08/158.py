data = ['hello.py', 'ex01.py', 'intro.hwp']

for file in data:
    file = file.split(".")[0]
    print(file)
