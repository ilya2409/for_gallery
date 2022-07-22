with open('my_test.txt', 'r') as f:
    lines = f.readlines()
    lines = lines[:-1]

with open('my_test.txt', 'w') as f:
    f.writelines(lines)
