print("""Список предоставляемых функций:

добавить запись: post
удалить запись: delete

""")

hello = str(input("Пишите: "))

while(True):

    if hello == "post":
        zagl = str(input("Введите заголовок: "))
        text = str(input("Введите текст: "))
        
        with open('my_test.html', 'r') as f:
            lines = f.readlines()
            lines = lines[:-3]
            
        with open('my_test.html', 'a') as f:
            f.writelines('\n' + f"<h3>{zagl}</h3>" + '\n' + f"<p>{text}</p>")

    elif hello == "delete":
        with open('my_test.txt', 'r') as f:
            lines = f.readlines()
            lines = lines[:-1]

        with open('my_test.txt', 'w') as f:
            f.writelines(lines)

    else:
        print("ERROR")
