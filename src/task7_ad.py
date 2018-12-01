import json

dollars10_18 = [30.16, 29.32, 29.89, 30.30, 36.04, 70.22, 83.59, 58.29, 62.41]


def rasschet_stoimosti_with_dict(dollars10_18, stoimost_pomesheniya=20000, stoimost_arendy_kvadrata=50, kvadraty=95):
    dinanica_cen = 0
    dinamica_arendy = 0
    obsluga = 0
    base_cena = 20000
    god = 2010
    # Создаем переменную и определяем ее как словарь. То есть все данные в итоге у нас будут занесенны в словарь
    result = {}
    for N in dollars10_18:
        dinanica_cen = stoimost_pomesheniya * N
        dinamica_arendy = stoimost_arendy_kvadrata * kvadraty * N
        obsluga = (dinanica_cen/100) * 20
        profit = dinanica_cen - obsluga + dinamica_arendy
        # print('В {} году стоимость помещения была равна {} рублей. '
        #       'Стоимость аренды равнялась {} рублей. Обслуживание его обошлось в {} рублей. '
        #       'В итоге профит от подорожания жилья и сдачи его стоставил {} рублей.'
        #       .format(god, dinanica_cen, dinamica_arendy, obsluga, profit))
        # Создаем переменную template в которую будем заносить все результаты вычислений нашей функции как элементы словаря.
        # В этом случае переменная будет каждый раз создаваться заного и новая ссылка в словаре создается заного, а не копируется
        template = dict(
            god=god,
            dinanica_cen=dinanica_cen,
            dinamica_arendy=dinamica_arendy,
            obsluga=obsluga,
            profit=profit
        )
        # Сформерованный словарь с результатами template я добавляю как значение для ключа god в словарь результатов result
        result[god]=template
        #print('В {} году стоимость помещения была равна {} рублей. Стоимость аренды равнялась {} рублей. Обслуживание его обошлось в {} рублей. В итоге профит от подорожания жилья и сдачи его стоставил {} рублей.'.format(god, dinanica_cen, dinamica_arendy, obsluga, profit))
        dict1 = {'god' : god, 'dinanica_cen' : dinanica_cen, 'dinamica_arendy' : dinamica_arendy, 'obsluga' : obsluga, 'profit' : profit}
        with open('result1.txt', 'w') as fp:
            json.dump(dict1, fp)

        god = god + 1
    return result


with open('result.txt', 'r') as fp:
    print(json.load(fp))

funct = rasschet_stoimosti_with_dict(dollars10_18)
print(funct)


def rasschet_stoimosti_with_list(dollars10_18, stoimost_pomesheniya=20000, stoimost_arendy_kvadrata=50, kvadraty=95):
    """
    Данная функция рассчитывает стоимость и доход с недвижимости и записывает данные в список,
    который она и выводит потом
    :param dollars10_18:
    :param stoimost_pomesheniya:
    :param stoimost_arendy_kvadrata:
    :param kvadraty:
    :return:
    """
    dinanica_cen = 0
    dinamica_arendy = 0
    obsluga = 0
    base_cena = 20000
    god = 2010
    # Создаем переменную и определяем ее как список. То есть все данные в итоге у нас будут занесенны в него
    result = []
    for N in dollars10_18:
        dinanica_cen = stoimost_pomesheniya * N
        dinamica_arendy = stoimost_arendy_kvadrata * kvadraty * N
        obsluga = (dinanica_cen/100) * 20
        profit = dinanica_cen - obsluga + dinamica_arendy
        # print('В {} году стоимость помещения была равна {} рублей. '
        #         #       'Стоимость аренды равнялась {} рублей. Обслуживание его обошлось в {} рублей. '
        #         #       'В итоге профит от подорожания жилья и сдачи его стоставил {} рублей.'
        #         #       .format(god, dinanica_cen, dinamica_arendy, obsluga, profit))
        # Создаем переменную template в которую будем заносить все результаты вычислений нашей функции как элементы списка.
        # В этом случае переменная будет каждый раз создаваться заного и новая ссылка в списке создается заного, а не копируется
        template = dict(
            god=god,
            dinanica_cen=dinanica_cen,
            dinamica_arendy=dinamica_arendy,
            obsluga=obsluga,
            profit=profit
        )
        # Сформерованный словарь с результатами template я добавляю как элемент списка результата result
        result.append(template)
        with open('result1.txt', 'w') as fp:
            json.dump(result, fp)

        god = god + 1
    return result


with open('result.txt', 'r') as fp:
    print(json.load(fp))


funct = rasschet_stoimosti_with_list(dollars10_18)
print(funct)






# with всегда хочет чтобы файс с которым он должен работать имел название


