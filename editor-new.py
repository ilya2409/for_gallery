a = str(input())

with open('aaa.txt', 'a') as f:
    f.writelines(str(a))

