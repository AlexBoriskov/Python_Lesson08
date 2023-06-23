file_name =  "Phone.txt"
my_file = open(file_name, "a+", encoding = "utf-8")
my_file.close()

def main_menu():
    print ("\nМеню\n")
    print ("1. Создание нового контакта")
    print ("2. Коррекция контакта")
    print ("3. Удаление данных")
    print ("4. Поиск телефона по Фамилии")
    print ("5. Поиск ФИО по телефону")
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
        print ("Поиск телефона по Фамилии")
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "5":
        print ("Поиск ФИО по телефону")
        enter = input ("Нажмите Enter для продолжения...")
        main_menu()
    elif choose == "6":
        print ("Показать телефонную книгу")
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

main_menu()
