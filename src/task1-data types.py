#создаем целое
a=int(10)
print(a)
#Создаем дробное
b=float(9.7)
print(b)
#Создаем строку
c=str('10')
print(c)
#Создаем массив
d=list()
#Добавляем в массив целое число
d.append(10)
#добавляем в массив дробоное число
d.append(10.45)
#Добавляем в массив строку
d.append('string0')
print(d)
#Создаем тупл
t=tuple()
#Менем тупл на лист, чтобы добавить туда элементы
t1=list(t)
#Добавляем в лист элементы и меняем обратно на тупл
t1=[12,'13',12.13]
t=list(t1)
print(t)
#Проверяем является ли t листом
if isinstance(t,list):
    print('Yes')
else:
    print('no')
#Меняем int на str
aa1=str(a)
print(aa1)
#Проверяем
if isinstance(aa1,str):
    print('Yes')
else:
    print('no')
#Меняем float на int
aa2=int(b)
print(aa2)
#Проверяем
if isinstance(aa2,int):
    print('Yes')
else:
    print('no')
#Меняем str на float
aa3=float(c)
print(aa3)