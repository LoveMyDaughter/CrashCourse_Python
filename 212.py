# 212 Користувач вводить з клавіатури число - програма повинна показати скільки
# в даному числі цифр. Число вводиться повністю в одну змінну. Примітка: Наприклад,
# користувач ввів число 11123445555. На екрані має з'явитися повідомлення про те,
# що в числі 5 цифр.

number = input("Enter number: ")
unique_digits = set(number)
print(len(unique_digits))