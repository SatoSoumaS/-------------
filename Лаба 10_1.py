pets = dict()
pet_name = input("Имя питомца: ")
pet_view = input(f"Введите вид питомца {pet_name}: ")
pet_age = int(input(f"Введите возраст питомца {pet_name}: "))
pet_user = input(f"Введите владельца питомца {pet_name}: ")
if pet_age % 10 == 1 and pet_age % 100 != 11:
    suffix = "год"
elif pet_age % 10 in [2, 3, 4] and not (pet_age % 100 in [12, 13, 14]):
    suffix = "года"
else:
    suffix = "лет"
pet_info = {
"Вид питомца ": pet_view,
"Возраст питомца ": f"{pet_age} {suffix}",
"Владелец питомца ": pet_user
}
pets[pet_name] = pet_info
print(pets)