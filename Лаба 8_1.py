n = int(input("Ведите кол-во чисел: "))
list = []
for i in range(n):
    a = int(input("Введите значение больше 1, и меньше 10000: " ))
if a>=1 and a<=10000:
    list.append(a)
else:
    print('Введите другое значение')
print(list)
print(list[::-1])