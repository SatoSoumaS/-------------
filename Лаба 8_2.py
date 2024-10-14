n = int(input("Введите количество чисел >=1 и <=1000000 "))
list = []
for i in range(n):
    a = int(input("Введите значение больше 1, и меньше 10000: " ))
if a >=1 and a <=100000:
    list.append(a)
else:
    print("Введите верное число")
a = list.pop(-1)
list.insert(0, a)
print(list)