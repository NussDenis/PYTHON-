# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def write_data_add(data):
    fl = True
    while fl:
        st = input("Введите ФИО и телефон через пробел:->")
        fl = chek_str(st)

    data.append('\n' + str(len(data)) + ';' + st.title().replace(' ', ';'))
    with open('file.xls', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("\n-> Файл сохранен.")
    return data


def changes_data(data): # изменение адресата по номеру
    fl = True
    temp = []
    coun = -1

    while fl:
        num = input(
            "Для изменения введите номер позиции в телефонном справочнике:->")
        fl = not (num.isdigit())
        if fl:
            print("Ввод не верный")

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][0] == num:
                    temp = data[i]
                    coun = i
        if coun == -1 and num.isdigit():
            print("Введенного номера нет в списке.")
            fl = True

    temp = temp.split(';')

    print(f"Запись № {num} на изменение: {temp}")
    f = True
    while f:
        st = input("Введите новую запись, ФИО и телефон через пробел:->")
        f = chek_str(st)

    temp = str(coun) + ';' + st.title().replace(' ', ';')

    for i in range(len(data)):
        if i == coun:
            data[i] = temp + '\n'

    with open('file.xls', 'w', encoding='utf-8') as file:
        for datas in data:
            file.writelines(datas)
    return data


def write_data(data): # запись данных в файл
    with open('file.xls', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("\n-> Файл сохранен.")


def del_data(data): # удаление всех адресатов
    with open('file.xls', 'w+', encoding='utf-8') as file:
        file.write('№ п/п; Фамилия; Имя; Отчество; Телефон')
    with open('file.xls', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def read_data(): # чтение данных из файла
    with open('file.xls', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data


def screen_data(data): # печать красиво
    st = []
    for j in range(len(data)):
        st.append(data[j].split(';'))
    for i in range(len(st)):
        print(
            f"{st[i][0]}\r\t{st[i][1]}\r\t\t\t{st[i][2]}\r\t\t\t\t\t{st[i][3]}\r\t\t\t\t\t\t\t{st[i][4]}", end='')


def search_data(data):  # поиск адресата
    st = []
    flag = True
    for j in range(len(data)):
        st.append(data[j].split(';'))
    while flag:
        stf = input('Для поиска введите Фамилию, Имя, Отчество или телефон:->')
        stx = []
        fl = False
        for el in st:
            for i in range(len(el)):
                if el[i].lower() == stf.lower():
                    stx.append(el)
                    fl = True

        if fl:
            print("\tВ справочнике информация найдена:")
            for i in range(len(stx)):
                print(
                    f"{stx[i][0]}\r\t{stx[i][1]}\r\t\t     {stx[i][2]}\r\t\t\t\t{stx[i][3]}\r\t\t\t\t\t\t{stx[i][4]}", end='')
            print()
        else:
            print(f"В справочнике с такими данными '{stf}' информации нет.")
        print("Продолжить поиск?")
        outdef = input(
            "Если 'Да', нажмите 'Y'. Выход в главное меню, нажмите 'Enter'->")
        if outdef.lower() == 'y' or outdef.lower() == 'н':
            flag = True
        else:
            flag = False


def del_user_data(data): # удаление адресата

    fl = flag = True
    temp = []
    coun = -1
    len_data = len(data)

    while flag:
        while fl:
            num = input(
                "Для удаления адресата введите номер позиции в телефонном справочнике:->")
            fl = not (num.isdigit())
            if fl:
                print("Ввод не верный")

            for i in range(len(data)):
                for j in range(len(data[i])):
                    if data[i][0] == num:
                        temp = data[i]
                        coun = n = i
            if coun == -1 and num.isdigit():
                print("Введенного номера нет в списке.")
                fl = True

        data.pop(coun)
        st = []
        for i in range(coun, len(data)):
            st.append(data[i].split(';'))

        for i in range(len(st)):
            st[i][0] = str(coun)
            coun += 1
        sty = []
        for el in st:
            sty.append(str(el).strip('[]').replace("'", '').replace(
                ' ', '').replace(',', ';').replace('\\n', '\n'))

        for i in range(len(sty)):
            data[n] = sty[i]
            n += 1

        temp = temp.split(';')

        print(f"Запись № {num} на удаление: {temp}")
        print("Продолжить удаление?")
        outdef = input(
            "Если 'Да', нажмите 'Y'. Выход в главное меню, нажмите 'Enter'->")
        if outdef.lower() == 'y' or outdef.lower() == 'н':
            flag = True
        else:
            flag = False
        if len_data == int(num) + 1:
            data[-1] = data[-1].strip()

    with open('file.xls', 'w', encoding='utf-8') as file:
        for datas in data:
            file.writelines(datas)
    print("\n-> Файл сохранен.")
    return data


def chek_str(st, n=3):  # проверка ввода данных
    f = True
    sr = st.split()
    sr = len(list(filter(lambda x: len(x) > n, sr)))
    if sr == 4:
        f = False
    else:
        print("Данные введены не корректно.")
    return f


def main():
    flag = True
    temp = ''
    data = read_data()
    while flag:
        print('\n- ---------- Т е л е ф о н н ы й  с п р а в о ч н и к ----------- -')
        screen_data(data)
        print()
        print("\nДобавления нового адресата -> введите 'A'")
        if len(data) > 1:
            print("Изменение адресата: --------> введите 'S'")
            print("Поиск адресата: ------------> введите 'F'")
            print("Сохранение данных: ---------> введите 'W'")
            print("Удаления адресата: ---------> введите 'D'")
            print("Новый справочник: ----------> введите 'P'")
        print("Выход из программы: --------> введите 'Q'")
        temp = input('Введите данные:->')
        if temp.lower() == 'q' or temp.lower() == 'й':
            flag = False
            print('Выход из программы!')
        elif temp.lower() == 'a' or temp.lower() == 'ф':  # добавление
            data = write_data_add(data)
        elif temp.lower() == 's' or temp.lower() == 'ы' and len(data) > 1:  # изменение
            data = read_data()
            data = changes_data(data)
        elif temp.lower() == 'f' or temp.lower() == 'а' and len(data) > 1:  # поиск
            search_data(data)
        elif temp.lower() == 'w' or temp.lower() == 'ц' and len(data) > 1:  # сохранение
            write_data(data)
        elif temp.lower() == 'd' or temp.lower() == 'в' and len(data) > 1:  # удаление адресата
            data = del_user_data(data)
        elif temp.lower() == 'p' or temp.lower() == 'з':  # новый справочник
            data = del_data(data)


if __name__ == '__main__':
    main()