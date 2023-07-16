data = ['intra.h', 'intra.c', 'define.h', 'run.py']

for file in data:
    last = file.split(".")[1]
    if last == 'h':
        print(file)