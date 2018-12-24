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


class ppl_base():
    def __init__(self):
        self.settings = "task9settings.json"
        self.emails = ["yahoo.com", "mail.ru", "gmail.com", "hotmail.com", "icloud.com", "rambler.com"]

    def get_names(self):
        if os.path.exists(self.settings):
            if os.path.isfile(self.settings):
                with open(self.settings, "r") as fp:
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


    def get_last_names(self):
        if os.path.exists(self.settings):
            if os.path.isfile(self.settings):
                with open(self.settings, "r") as fp:
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


    def get_list_of_logins(self):
        first_names = self.get_names()
        last_names = self.get_last_names()
        logins = []
        for index in range(0, len(first_names)):
            first_name = first_names[index].lower()
            first_letter = first_name[0]
            last_name = last_names[index].lower()
            login = ".".join([first_letter, last_name])
            logins.append(login)
        return logins

    def get_random_login(self):
        self.random_login = self.get_list_of_logins()[randint(0, len(self.get_list_of_logins())-1)]
        return self.random_login

    def get_random_email(self):
        random_domen = self.emails[randint(0, len(self.emails)-1)]
        random_email = self.random_login + "@" + random_domen
        return random_email

    def create_random_password(self):
        password = ""
        random = randint(8, 12)
        leight = range(0, random)
        for char in leight:
            random_char = randint(0, 9)
            password = password + str(random_char)
        return password

    def work(self):
        n = 10
        x = 0
        while x != n:
            final_login = self.get_random_login()
            final_password = self.create_random_password()
            final_email = self.get_random_email()
            print("Логин: {}, Пароль: {}, Электронная почта: {}".format(final_login, final_password, final_email))
            x += 1
        return



instance = ppl_base()
instance.work()

