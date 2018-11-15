
v=input('Введите число ')
try:
    s=int(v)
    if s%2==0:
        print('Четное')
    else:
        print('Не четное')
except:
    print('Это вообще не число')

