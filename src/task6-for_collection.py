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


task6_list = [35,45,190,30,90,-170, 160]

def maximum(task6_list):
    mulka = -10000
    for element_1 in task6_list:
        if element_1 > mulka:
            mulka = element_1
    return mulka

print(maximum(task6_list))

def minimum(task6_list):
    mulka2 = 10000000000
    for element in task6_list:
        if element < mulka2:
            mulka2 = element
    return mulka2
print(minimum(task6_list))

def srendee(task6_list):
    mulka0 = 0
    for element_2 in task6_list:
        mulka0 = mulka0 + element_2
        srenyaya_mulka = mulka0 / len(task6_list)
    return srenyaya_mulka
print(srendee(task6_list))

