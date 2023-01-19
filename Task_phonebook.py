import os
from datetime import time

fileName = "phonebook.txt"


def clear_screen():
    os.system("cls")

def search_data():
    clear_screen()
    while (True):
        answer = input('Строка поиска(\'\' -выход) :>')
        if answer == "": return
        result = []
        with open('phonebook.txt', 'r', encoding='utf8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
                result = list(filter(lambda line: answer in line, result))
        for printdata in result:
            output_data_string(printdata)

def output_data_string(printdata):
    parse_data = printdata.split(',')
    template = 'Фамилия: {0}\nИмя: {1}\nОтчество: {2}\nТелефон: {3}\n'
    print(template.format(parse_data[0], parse_data[1], parse_data[2], parse_data[3]))


def save_data_to_file(data_to_save):
    data_to_save = ",".join(data_to_save) + "\n"
    print(data_to_save)
    with open('phonebook.txt', 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)


def print_data():
    count = 0
    with open('phonebook.txt', "r", encoding="utf8") as datafile:
        for line in datafile:
            count += 1
            print(":{:<3} ".format(count), end='')
            output_data_string(line.strip('\n'))
    return count


def print_all_data():
    count = print_data()
    input('Всего {} Записей.  Enter для выхода' .format(count))


def add_data():
    clear_screen()
    while True:
        print('Добавление записи("m"-выход)>:')
        last_name = input("Фамилия: ")
        if last_name == "m":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер Телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        save_data_to_file(data_to_save)


def del_data():
    while True:
        clear_screen()
        print("E - удаление по номеру записи\n"
              "W - удаление по поиску\n"
              "Q - выход")
        answer = input(">:").upper()
        match answer:
            case "E":
                del_data_by_number()
            case "W":
                del_data_by_search()
            case "Q":
                return
            case _:
                print("неверный ввод")
                time.sleep(1)


def del_data_by_search():
    clear_screen()
    while True:
        answer = input("Строка поиска для удаления('m'-выход)>:")
        if answer == 'm':
            return
        found_records = search_data(answer)
        if len(found_records) == 0:
            print("нет записей для удаления")
        else:
            print("найдены записи:")
            for printdata in found_records:
                output_data_string(printdata)
            if input('удаляем [Y-да/..-нет]').upper() == "Y":
                phonedata = ""
                with open('phonebook.txt', "r", encoding="utf8") as datafile:
                    for line in datafile:
                        if answer in line:
                            continue
                        phonedata += line

                with open('phonebook.txt', "w", encoding="utf8") as datafile:
                    datafile.write(phonedata)


def del_data_by_number():
    while True:
        clear_screen()
        print_data()
        answer = input("Номер записи для удаления(Q - выход)>: ")
        if answer.upper() == "Q":
            return
        if not answer.isnumeric():
            continue
        answer = int(answer)
        print(answer)
        phonedata = ""
        count = 0
        with open('phonebook.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                count += 1
                if answer == count:
                    continue
                phonedata += line

        with open('phonebook.txt', "w", encoding="utf8") as datafile:
            datafile.write(phonedata)


if __name__ == "__main__":
    # основной блок
    menu = (f"Телефонный справочник.\n\n"
            "Введите команду\n"
            "Z - Вывод данных\n"
            "X - Добавление записи\n"
            "C - Поиск\n"
            "V - Удаление записи\n"
            "N - Выход\n")
    while True:
        clear_screen()
        print(menu)
        answer = input(">:").upper()
        match answer:
            case "Z":
                # вывод данных
                print_all_data()

            case "X":
                # добавление данных
                add_data()

            case "C":
                # поиск
                search_data()

            case "V":
                # удаление данных
                del_data()

            case "N":
                # выход
                exit(0)

            case _:
                print("неверный ввод")
                time.sleep(1)