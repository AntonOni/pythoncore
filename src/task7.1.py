import json
import os

# Определим имя файла с настройками
settings_file_name = 'settings.json'

class procent_calc:

    def __init__(self):
        pass

    @staticmethod
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

    @staticmethod
    def work_with_proc(readed_file):
        keys = readed_file.keys()
        for i in keys:
            if i == "procent_file":
                procent_file_content = readed_file.get(i, [])
                return procent_file_content
        else:
            print("Not found")

    @staticmethod
    def get_znacheniya(procent_file_content):
        list_znachen = []
        keys = procent_file_content.keys()
        for k in keys:
            znach = procent_file_content[k]
            list_znachen.append(znach)
        return list_znachen

    @staticmethod
    def izvlechenie_procentov(list_znachen):
        list_procentov = []
        for i in list_znachen:
            with open(i, "r") as fp:
                try:
                    content = fp.read().split(", ")
                    list_procentov += content
                except:
                    print("Невозможно прочесть")
        return list_procentov

    def rasschet_stoimosti_with_dict(self, list_procentov):
        dinanica_cen = dinamica_arendy = obsluga = 0
        base_cena = 20000
        god = 2010
        result = {}
        for N in list_procentov:
            dinanica_cen = self.stoimost_pomesheniya * float(N)
            dinamica_arendy = self.stoimost_arendy_kvadrata * self.kvadraty * float(N)
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
            with open(self.output_file, 'a') as fp:
                print("  [+] append data from function "
                      "rasschet_stoimosti_with_dict to file"
                      " {}".format(self.output_file))
                json.dump(template, fp)
                fp.write("\n")
            god = god + 1
        return result

    @staticmethod
    def output_file_deleter(output_file):
        if os.path.exists(output_file):
            print('remove: {}'.format(output_file))
            os.remove(output_file)

    def work(self):
        readed_file = self.reading_func(settings_file_name)
        self.procent_file_content = self.work_with_proc(readed_file)
        self.output_file = readed_file.get("output_file", "output_file")
        self.list_znachen = self.get_znacheniya(self.procent_file_content)
        self.stoimost_pomesheniya = readed_file.get("stoimost_pomesheniya", 20000)
        self.list_procentov = self.izvlechenie_procentov(self.list_znachen)

        self.stoimost_arendy_kvadrata = readed_file.get("stoimost_arendy_kvadrata", 50)
        self.kvadraty = readed_file.get("kvadraty", 95)
        print("[!] Call function: rasschet_stoimosti_with_dict...")
        self.output_file_deleter(self.output_file)



        funct = self.rasschet_stoimosti_with_dict(self.list_procentov)
        print(funct)
        print("[+] Complete...")


a = procent_calc()
b = a.work()
print(b)


# Выгружаем содержимое файла в переменную settings_file_content_as_json
# settings_file_content_as_json = get_settings_from_file(settings_file_name)

# Создаем переменные и в них загружаем по отдельности каждое значение из settings_file_content_as_json

# Читаем имя файла с процентами из переменной settings_file_content_as_json

# procent_file_name = settings_file_content_as_json.get("procent_file", "procents_data.csv")
#
# # procents = get_procents_from_file(procent_file_name)
#
# # Заполняем отдельно имя файла с результатами "ouput_file": "result_of_calcualtion.txt"
# output_file = ("ouput_file", "ouput_file")
#
# stoimost_pomesheniya = settings_file_content_as_json.get("stoimost_pomesheniya", 20000)
#
# stoimost_arendy_kvadrata = settings_file_content_as_json.get("stoimost_arendy_kvadrata", 50)
#
# kvadraty = settings_file_content_as_json.get("kvadraty", 95)









