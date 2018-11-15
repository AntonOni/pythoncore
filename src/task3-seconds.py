#Задача написать программу которая рассчитывает день, час, минуту, секунду исходя из количества заданных секунд
sec = 90
seconds_in_minutes = 60
seconds_in_hour = 60*seconds_in_minutes
seconds_in_day = 24*(60*seconds_in_minutes)
minutes_in_hour = 60
hour_in_day = 24
minutes_in_day = hour_in_day * minutes_in_hour

minutes = sec / seconds_in_minutes #Целое отделение 90/60 = 1
seconds = sec % seconds_in_minutes #Остаточная часть 90/60 = 30


def sqr(a):
    """
    Краткое описвание
    :param a: входное число
    :return: результат
    """
    result = a * a
    return result

def get_hours_from_minutes(minutes):
    """

    :param minutes:
    :return:
    """
    hours = minutes / minutes_in_hour
    return int(hours)


def get_minutes_from_seconds(seconds):
    """
    Get minutes from seconds
    :param seconds: seconds
    :return: minutes
    """
    minutes = seconds / seconds_in_minutes
    return int(minutes)

def get_residual_seconds(seconds):
    """

    :param seconds:
    :return:
    """
    sec = seconds % seconds_in_minutes
    return int(sec)

def input_number_from_user():
    v = input('Введите число ')
    try:
        s = int(v)
        return s
    except:
        print('Это вообще не число, будет возвращен нуль')
        return 0

def correct_minutes_result(result):
    """

    :param result:
    :return:
    """
    if result == seconds_in_minutes:
        return 0
    return result

def correct_hours_result(result):
    """

    :param result:
    :return:
    """
    if result == hour_in_day:
        return 0
    return result

print("проверяем")
m = input_number_from_user()
print('Введено число: {}'.format(m))

second = get_residual_seconds(m)
min = get_minutes_from_seconds(m)
hours = get_hours_from_minutes(min)
corrected_minutes = correct_minutes_result(min)

print('Проверяем получение часов')
print('Получить {} часов'.format(hours))

print('Проверяем полчение минут')
print('Получилось {} минут'.format(corrected_minutes))

print('Проверяем получение секунд')
print('Получить {} секунд'.format(second))












#Итого 1 минута 30 секунд

# заметка про деление
# СИмвол деления / работает по разному с разным типом чисел
# если хотя бы одно из двух чисел float то деление работает как ДЕЛЕНИЕ 190.0/60=3.16666
# Если ОБА числа целые (int) то деление работает как ЦЕЛАЯ ЧАСТЬ от деления 190/60=3
#
# % всегда работает как остаток от деления, но хотя бы с одним float оно дает на выходе float
# Если оба int оно дает int


