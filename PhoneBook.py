import os

file_name =  "Phone.txt"
my_file = open(file_name, "a+", encoding = "utf-8")
my_file.close()

def main_menu():
    print ("\nМеню\n")
    print ("1. Создание нового контакта")
    print ("2. Коррекция контакта")
    print ("3. Удаление данных")
    print ("4. Поиск телефона по Фамилии")
    print ("5. Поиск контакта по телефону")
    print ("6. Показать все контакты")
    print ("7. Выход")

    choose = input("\nВведите № действия: ")
    if choose == "1":
        new_contact()
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "2":
        print ("Коррекция контакта")
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "3":
        print ("Удаление контакта")
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == '4':
        find_phone()
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "5":
        find_contact()
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "6":
        all_contact()
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "7": print ("Пока.")
    else: 
        print ("Не была выбрана команда!")
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()

def new_contact ():
    second_name = input("Введите Фамилию: ")
    first_name = input ("Введите Имя: ")
    phone = input ("Введите номер телефона: ")
    emailID = input ("Введите почту: ")
    status = input ("Введите статус человека: ")
    contact = (second_name + " " + first_name + " " + phone + " " + emailID + " " + status + "\n")
    my_file = open(file_name, "a")
    my_file.write(contact)
    my_file.close()
    print ("Создан новый контакт!")

def all_contact():
    my_file = open(file_name, "r")
    if len (file_name) != 0:
        lines = my_file.readlines()
        for line in lines:
            print (line)
    else: print ("Нет контактов")
    my_file.close()

def find_contact():
    find_phone = input("Введите телефон для поиска: ")
    my_file = open(file_name, 'r')
    lines = my_file.readlines()
    for line in lines:
        if find_phone in line:
            print (line)
        else: print ("Нет такого контакта")
    my_file.close()

def find_phone():
    second_name = input("Введите фамилию для поиска: ")
    my_file=open(file_name, 'r')
    lines = my_file.readlines()
    for line in lines:
        line = line.split()
        if second_name in line:
            print (line[2])
        else: print ("Нет такой фамилии в книжке")
    my_file.close()

main_menu()
