
import random

def generate_one_number(min=0, max=100):
    return random.randint(min, max)

def generator(count=10, min=10, max=20):
    # define empty list for random numbers
    result = []
    # generate list of integer numbers just for for loop iterations, ex. 0, 1, 2, ..., count
    diapason = range(count)
    for i in diapason:
        # call function generate_one_number with input parameters min and max
        # min and max defines boundares of random function values: from min (include) to max (exclude)
        # and APPENDS generated value to result - which is a list of random numbers
        one_random_number = generate_one_number(min, max)
        result.append(one_random_number)
    # trace out result (list of random numbers)
    return result

#print("generate 15 numbers with default min and max: {}".format(generator(count=15)))
# print("generate numbers with min=3 and default count and max: {}".format(generator(min=3)))
# print("generate numbers with max=20 and default  count and min: {}".format(generator(max=20)))
# print("generate 5 numbers with default count: {}".format(generator(count=20, min=5)))
#print("generate 5 numbers with default count: {}".format(generator(count=20, min=3, max=50)))


#Задача. Генирайция случайного числа и будем просить пользователя угадать это число. Программа будет говорить больше/меньше загаданного числа, вышло ли число за пределы диапазона или он угадал.

# generate random number
# ask user for his number
# check this number if it less or greater than our random number
# or equal
# if it is less, say "ups it is less"
# if it is greater, say "wow it is greater"
# if it is equal, say "Ah! Got it!!!"
# repeat until equal

random_number = random.randint(0, 100)#Рандом выбирает число

while True:#Открывает цикл. True тут надо чтобы цикл работал (пока верно, работаем)
    try:#Тут ловим исключение чтобы вводили только цифры и наш цикл не сломался об исключение
        customer_input = input('Давайте поиграем, введите число ')#Запрашиваем у пользователя ввод
        int_customer_input = int(customer_input)#Преобразуем введеную строку в целое число
        if int_customer_input > random_number:#Условие если вверденое число больше загаданного рандомного
            print('Gretaer then expected')#Написать Больше чем ожидается
            continue#И вернуться у началу цикла
        elif int_customer_input < random_number:#Условие если введеное число меньше загаданного
            print('Less then expected')#Написать Меньше чем оживается
            continue#И вернуться у началу цикла
        else:#Все остальные случаи (А тут оставшийся случай может быть только равенство)
            print('Ugadal')#Написать угадал
            break#И прервать цикл
    except:#Если поймали любое исключение
        print('Вы ввели не число')#Пишем Вы ввели не число
        continue#И вернуться у началу цикла

