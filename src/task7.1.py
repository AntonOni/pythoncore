import json
import os

# Определим имя файла с настройками
settings_file_name = 'settings.json'


# def get_procents_from_file(procents_file):
#     if os.path.exists(procents_file):
#         if os.path.isfile(procents_file):
#             with open(procents_file, "r") as fp:
#                 try:
#                     procents_file_content = fp.read()
#                     procents_file_content_split = procents_file_content.split(", ")
#                     list_of_procents = []
#                     for _ in procents_file_content_split:
#                         try:
#                             list_of_procents.append(float(_))
#                         except:
#                             print("Нельзя сделать float")
#                     return list_of_procents
#                 except:
#                     print("Ошибка чтения")
#         else:
#             print("Это не файл")
#     else:
#         print("Такого пути нет")
#     return []



# Читаем файл
# Я проверяю наличие и тип файла с настройками
# Затем импортирую его содержимое как json
def get_settings_from_file(settings_file_name):
    if os.path.exists(settings_file_name):
        if os.path.isfile(settings_file_name):
            with open(settings_file_name, 'r') as fp:
                try:
                    settings_file_content_as_json = json.load(fp)
                    return settings_file_content_as_json
                except Exception as ex:
                    print('Got an exception {}'.format(ex))
        else:
            print('This is not a file')
    else:
        print('Path not exist')
    return {}


def rasschet_stoimosti_with_dict(total):
    dinanica_cen = dinamica_arendy = obsluga = 0
    base_cena = 20000
    god = 2010
    result = {}
    for N in total:
        dinanica_cen = stoimost_pomesheniya * N
        dinamica_arendy = stoimost_arendy_kvadrata * kvadraty * N
        obsluga = (dinanica_cen/100) * 20
        profit = dinanica_cen - obsluga + dinamica_arendy
        template = dict(
            god=god,
            dinanica_cen=dinanica_cen,
            dinamica_arendy=dinamica_arendy,
            obsluga=obsluga,
            profit=profit
        )
        result[god]=template
        with open("output_file", 'a') as fp:
            print("  [+] append data from function rasschet_stoimosti_with_dict to file {}".format(output_file))
            json.dump(template, fp)
            fp.write("\n")
        god = god + 1
    return result




# Выгружаем содержимое файла в переменную settings_file_content_as_json
settings_file_content_as_json = get_settings_from_file(settings_file_name)

# Создаем переменные и в них загружаем по отдельности каждое значение из settings_file_content_as_json

# Читаем имя файла с процентами из переменной settings_file_content_as_json

procent_file_name = settings_file_content_as_json.get("procent_file", "procents_data.csv")

# procents = get_procents_from_file(procent_file_name)

# Заполняем отдельно имя файла с результатами "ouput_file": "result_of_calcualtion.txt"
output_file = ("ouput_file", "ouput_file")

stoimost_pomesheniya = settings_file_content_as_json.get("stoimost_pomesheniya", 20000)

stoimost_arendy_kvadrata = settings_file_content_as_json.get("stoimost_arendy_kvadrata", 50)

kvadraty = settings_file_content_as_json.get("kvadraty", 95)


if os.path.exists("output_file"):
    os.remove("output_file")


print("[!] Call function: rasschet_stoimosti_with_dict...")
# funct = rasschet_stoimosti_with_dict(procents)
# print(funct)
print("[+] Complete...")



def reading_func(settings_file_name):
    if os.path.exists(settings_file_name):
        if os.path.isfile(settings_file_name):
            with open(settings_file_name, "r") as fp:
                try:
                    readed_file = json.load(fp)
                    return readed_file
                except:
                    print("Файл не читается")
        else:
            print("Нет файла")
    else:
        print("Нет пути")

readed_file = reading_func(settings_file_name)
print(readed_file)

print("1_____________________________________")

def work_with_proc(readed_file):
    keys = readed_file.keys()
    list_of_content = []
    for i in keys:
        if i == "procent_file":
            procent_file_content = readed_file.get(i, [])
            return procent_file_content
    else:
        print("Not found")

procent_file_content = work_with_proc(readed_file)
print(procent_file_content)

print("2_______________________________________")


def get_znacheniya(procent_file_content):
    list_znachen = []
    keys = procent_file_content.keys()
    for k in keys:
        znach = procent_file_content[k]
        list_znachen.append(znach)
    return list_znachen

list_znachen = get_znacheniya(procent_file_content)
print(get_znacheniya(procent_file_content))

print("3___________________________")

def izvlechenie(list_znachen):
    list_procentov = []
    for i in list_znachen:
        with open(i, "r") as fp:
            try:
                content = fp.read().split(", ")
                list_procentov += content
            except:
                print("Невозможно прочесть")
    return list_procentov

total = izvlechenie(list_znachen)
print(total)
