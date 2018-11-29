import json

dollars10_18 = [30.16, 29.32, 29.89, 30.30, 36.04, 70.22, 83.59, 58.29, 62.41]


def rasschet_stoimosti(dollars10_18, stoimost_pomesheniya=20000, stoimost_arendy_kvadrata=50, kvadraty=95):
    dinanica_cen = 0
    dinamica_arendy = 0
    obsluga = 0
    base_cena = 20000
    god = 2010
    for N in dollars10_18:
        dinanica_cen = stoimost_pomesheniya * N
        dinamica_arendy = stoimost_arendy_kvadrata * kvadraty * N
        obsluga = (dinanica_cen/100) * 20
        profit = dinanica_cen - obsluga + dinamica_arendy
        print('В {} году стоимость помещения была равна {} рублей. Стоимость аренды равнялась {} рублей. Обслуживание его обошлось в {} рублей. В итоге профит от подорожания жилья и сдачи его стоставил {} рублей.'.format(god, dinanica_cen, dinamica_arendy, obsluga, profit))
        dict1 = {'god' : god, 'dinanica_cen' : dinanica_cen, 'dinamica_arendy' : dinamica_arendy, 'obsluga' : obsluga, 'profit' : profit}
        with open('result.txt', 'w') as fp:
            json.dump(dict1, fp)
        with open('result.txt', 'r') as fp:
            print(json.load(fp))
        god = god + 1
    return profit

rasschet_stoimosti(dollars10_18)

