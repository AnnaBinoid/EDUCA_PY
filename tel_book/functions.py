import re



def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding= 'utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')

    with open('book.txt', 'a', encoding= 'utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    
    with open('book.txt', 'r', encoding= 'utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])



def delete_data():
    FIND = input("Введите: ")
    INFILE = "book.txt"
    OUTFILE = "output.txt"

    f = open('output.txt', 'w')  # Очистка первого листа
    f.close()
    f = open('output.txt', 'w')

    with open(INFILE, encoding="utf-8") as infile, open(OUTFILE, "w", encoding="utf-8") as outfile:
        for line in infile:
            if FIND not in line:
                outfile.write(line)

    f = open('book.txt', 'w')  # Очистка первого листа
    f.close()
    f = open('book.txt', 'w')

    with open('output.txt','r', encoding="utf-8") as firstfile, open('book.txt','a', encoding="utf-8") as secondfile:
       
    # read content from first file
        for line in firstfile:
                # append content to second file
                secondfile.write(line)

def change_data():
    FIND = input("Введите: ")
    INFILE = "book.txt"
    OUTFILE = "output.txt"

    f = open('output.txt', 'w')  # Очистка первого листа
    f.close()

    with open(INFILE, encoding="utf-8") as infile, open(OUTFILE, "w", encoding="utf-8") as outfile:
        for line in infile:
            if FIND not in line:
                outfile.write(line)
            else:
                fio = input('Введите ФИО: ')
                tel_number = input('Введите номер телефона: ')
                f = open('output.txt', 'a', encoding= 'utf-8')
                f.write(f'{fio} | {tel_number}')
    
    f = open('book.txt', 'w')  # Очистка первого листа
    f.close()

    with open('output.txt','r', encoding="utf-8") as firstfile, open('book.txt','a', encoding="utf-8") as secondfile:
       
    # read content from first file
        for line in firstfile:
                # append content to second file
                secondfile.write(line)
                    
while True:
    print('1. вывод , 2. добавление, 3. поиск, 4. изменение, 5. удаление')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        change_data()
    elif mode == 5:
        delete_data()
    else:
        break