#list_of_elements = [1,2,3,4,5,90]

# for el in list_of_elements:
#     el = el * 2
#     print(el)
#     print(list_of_elements)

# for number in range(0, len(list_of_elements)):
#     list_of_elements[number] = list_of_elements[number] * 2
#     print('Номер в массиве {}   отслеживаем измениения в массиве {}'.format(number, list_of_elements))


#for number, value in enumerate(list_of_elements):
    #enumerate генерирует на каждой инерации цикла
    #пару чисел: number - это порядковый номер элемена в массиве
    #value - это значение элемента в массиве
    #И index и value будут другими на кажой последующей итерации, то есть изменяться каждый прогон
#    list_of_elements[number] = value * 2 #Берет номер эдемена в массиве и умножает значение которое стоит под этим номером в массиве на два
#    print('Номер в массиве {}  отслеживаем измениения в массиве {}'.format(number, list_of_elements))


# task6_list = [35,45,190,30,90,-170, 160]
#
# def maximum(task6_list):
#     mulka = -10000
#     for element_1 in task6_list:
#         if element_1 > mulka:
#             mulka = element_1
#     return mulka
#
# print(maximum(task6_list))
#
# def minimum(task6_list):
#     mulka2 = 10000000000
#     for element in task6_list:
#         if element < mulka2:
#             mulka2 = element
#     return mulka2
# print(minimum(task6_list))
#
# def srendee(task6_list):
#     mulka0 = 0
#     for element_2 in task6_list:
#         mulka0 = mulka0 + element_2
#         srenyaya_mulka = mulka0 / len(task6_list)
#     return srenyaya_mulka
# print(srendee(task6_list))
#
#
#
# new_list = [-20, 12, 20, -35, 10, -1, 15]
#
#
# def summa_modul(new_list):
#     summa_mod = 0
#     for i in new_list:
#         if i > -2.5:
#             summa_mod = abs(i) * abs(i) + summa_mod
#     return summa_mod
# print(summa_modul(new_list))
#
# def summa_na_5(new_list):
#     summa_celih_na_5 = 0
#     for x in new_list:
#         if x%5 == 0:
#             summa_celih_na_5 = x + summa_celih_na_5
#     return summa_celih_na_5
# print(summa_na_5(new_list))
#
#
#
# godovie = [6.25, 6.12, 6.73, 7.15, 8.17]
# def sberbank(godovie):
#     vklad_base = vklad = 10000
#     profit = 0
#
#     for proc in godovie:
#         vklad = (vklad / 100) * proc + vklad
#
#     return vklad - vklad_base
# print(sberbank(godovie))


from datetime import datetime

godovie = [6.25, 6.12, 6.73, 7.15, 8.17]
def sberbank_popolnen(godovie, popolnenie=10000, base_vklad=10000):
    vklad = base_vklad
    period = 0
    profit = 0
    chistaya_pribl = 0
    god = datetime.now().year
    for proc in godovie:
        profit = vklad / 100 * proc
        chistaya_pribl = chistaya_pribl + profit
        vklad = vklad + profit
        if period != 0:
            vklad = vklad + popolnenie
            base_vklad = base_vklad + base_vklad
        print('В {} году размер вклада составит {} , профит {}, а чистая прибыль {} р.'.format(god, vklad, profit, chistaya_pribl))
        period = period + 1
        god = god + 1

    return vklad - base_vklad

sberbank_popolnen(godovie)