n = int(input('Введите количество чисел: '))
numbers = [int(input('Введите число: ')) for i in range(n)]
print("Количество раз ты ввел ноль: ",numbers.count(0))
