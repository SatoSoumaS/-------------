N = int(input("Введите количество чисел: "))
numbers = list(map(int, input(f'Введите через пробел {N} чисел: ').split()))
number_list = set(numbers)
print(len(number_list))