# # Сгенерировать базу пользователей собейжащую ключи
# names = []
# last_names = []
# logins = []
# login = первая буква от имени + точка + фамилия
# emails = ["yahoo.com", "mail.ru", "gmail.com", "hotmail.com", "icloud.com", "rambler.com"]
# # email = логин + @ + рандомный домен
# passwords = []
# # Password =  рандомные длинна пароля + рандомные числа в пароле
# age = []

import json
from random import randint
import os


class PeopleBaseGenerator():
    def __init__(self):
        self.__settings = "task9settings.json"
        self.__emails = ["yahoo.com", "mail.ru", "gmail.com", "hotmail.com", "icloud.com", "rambler.com"]
        self.__random_login = ""

    def __get_names(self):
        if os.path.exists(self.__settings):
            if os.path.isfile(self.__settings):
                with open(self.__settings, "r") as fp:
                    try:
                        loaded_file = json.load(fp)
                        items = loaded_file.values()
                        for i in items:
                            if i == "names.csv":
                                with open(i,"r") as fp:
                                    try:
                                        content = fp.read()
                                        names = content.split(", ")
                                        return names
                                    except:
                                        print("Имена прочесть нельзя")
                    except:
                        print("Нельзя прочесть файл")
            else:
                print("Не файл")
        else:
            print("Нет директории")


    def __get_last_names(self):
        if os.path.exists(self.__settings):
            if os.path.isfile(self.__settings):
                with open(self.__settings, "r") as fp:
                    try:
                        loaded_file = json.load(fp)
                        items = loaded_file.values()
                        for i in items:
                            if i == "last_names.csv":
                                with open(i,"r") as fp:
                                    try:
                                        content = fp.read()
                                        last_names = content.split(", ")
                                        return last_names
                                    except:
                                        print("Фамилии прочесть нельзя")
                    except:
                        print("Нельзя прочесть файл")
            else:
                print("Не файл")
        else:
            print("Нет директории")

# def get_login():
#     login = ""
#     for i in get_names():
#         first_letter = i[0]
#         last_names = get_last_names()
#         random_last_name = last_names[randint(0, len(last_names)-1)]
#         login = first_letter + "." + random_last_name
#         print(login)
# get_login()

    def random_number(self):
        random_number = randint(0, 100)
        return random_number

    def __get_list_of_logins(self):
        first_names = self.__get_names()
        last_names = self.__get_last_names()
        logins = []
        for index in range(0, len(first_names)):
            first_name = first_names[index].lower()
            first_letter = first_name[0]
            last_name = last_names[index].lower()
            login = ".".join([first_letter, last_name])
            logins.append(login)
        return logins

    def __get_random_login(self):
        self.__random_login = self.__get_list_of_logins()[randint(0, len(self.__get_list_of_logins())-1)]
        return self.__random_login

    def __get_random_email(self):
        random_domen = self.__emails[randint(0, len(self.__emails)-1)]
        random_email = self.__random_login + "@" + random_domen
        return random_email

    def __create_random_password(self):
        password = ""
        random = randint(8, 12)
        leight = range(0, random)
        for char in leight:
            random_char = randint(0, 9)
            password = password + str(random_char)
        return password

    def __random_age(self):
        random_age = randint(18, 99)
        return random_age

    def work(self):
        n = 10
        x = 0
        while x != n:
            final_login = self.__get_random_login()
            final_password = self.__create_random_password()
            final_email = self.__get_random_email()
            random_age = self.__random_age()
            print("Логин: {}, Пароль: {}, Электронная почта: {}, Возраст {}".format(final_login, final_password, final_email, random_age))
            x += 1
        return

class Credit_cards():
    def __init__(self):
        pass

    def __card_number_gen(self):
        leight = range(0, 16)
        cc_number = ""
        for _ in leight:
            random_number = randint(0, 9)
            cc_number += str(random_number)
        return cc_number

    def __exp_date_gen(self):
        month = str(randint(1, 12))
        year = str(randint(18, 24))
        date = month + "/" + year
        return date

    def __cvs_gen(self):
        cvs = randint(000, 999)
        return cvs

    def work(self):
        n = 0
        x = 10
        while n != x:
            card_number = self.__card_number_gen()
            exp_date = self.__exp_date_gen()
            cvs = self.__cvs_gen()
            print("Номер кредитной карты: {}, Срок годности: {}, CSV: {}".format(card_number, exp_date, cvs))
            n += 1

class Auto_gen():

    def __init__(self):
        self.marks = ["Lada", "Audi", "BMW", "Mersedes", "Reno"]
        self.vin = ""
        self.number = ""

    def __number_or_letter(self):
        random_number = randint(0, 100)
        if random_number >= 50:
            random_symbol = randint(0, 9)
            return str(random_symbol)
        if random_number < 50:
            list_of_bukv = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
            random_bukva = list_of_bukv[randint(0, len(list_of_bukv)-1)]
            return str(random_bukva)

    def __gen_random_mark(self):
        random_mark = self.marks[randint(0, len(self.marks)-1)]
        return random_mark

    def __gen_random_vin(self):
        self.vin = ""
        shchet = range(0, 16)
        for _ in shchet:
            self.vin = self.vin + self.__number_or_letter()
        return self.vin

    # def get_random_number(self):


    def work(self):
        x = 10
        n = 0
        while n != x:
            random_mark = self.__gen_random_mark()
            random_vin = self.__gen_random_vin()

            print("Марка: {}, vin: {}".format(random_mark, random_vin))
            n += 1

class Porodistiye_zveri():
    def __init__(self):
        self.list_of_zveri = ["Cat", "Dog", "MblIIIb", "OJIeHb", "KOZA", "CBUHKA", "VOLK"]
        self.cveta = ["blue", "yellow", "black", "white", "Orange", "Navy"]
        self.ceriya_passporta = ""
        self.nomer_passporta = ""
        self.kem_vidan = ["Otdeleniem UFMS po Moskve", "Otdeleniem v Rostove", "V Piterskom passportnom stole", "Na rinke v Taganroge"]

    def __get_random_zver(self):
        zver = self.list_of_zveri[randint(0, len(self.list_of_zveri)-1)]
        return zver

    def __get_random_cvet(self):
        cvet = self.cveta[randint(0, len(self.cveta)-1)]
        return cvet

    def __get_ceriya_passporta(self):
        leigh = range(0, 4)
        self.ceriya_passporta = ""
        for _ in leigh:
            cifra = randint(0, 9)
            self.ceriya_passporta = self.ceriya_passporta + str(cifra)
        return self.ceriya_passporta

    def __get_random_nomer(self):
        n = 6
        x = 0
        self.nomer_passporta = ""
        while x != n:
            nomer = randint(0, 9)
            self.nomer_passporta = self.nomer_passporta + str(nomer)
            x += 1
        return self.nomer_passporta

    def __vidan_kem(self):
        vidan = self.kem_vidan[randint(0, len(self.kem_vidan)-1)]
        return vidan

    def work(self):
        leigh = range(0, 20)
        for _ in leigh:
            zver = self.__get_random_zver()
            cvet = self.__get_random_cvet()
            ceriya_pass = self.__get_ceriya_passporta()
            nomer_pass = self.__get_random_nomer()
            kem_vidan = self.__vidan_kem()
            print("Животное: {}, Цвет: {}, Пасспортные данные: серия: {}, номер: {}, выдан: {}".format(zver, cvet, ceriya_pass, nomer_pass, kem_vidan))

