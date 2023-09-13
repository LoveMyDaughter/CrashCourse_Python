# 214 Користувач вводить з клавіатури число, необхідно показати на екран суму
# його цифр. Примітка: Наприклад, користувач ввів число 12345. На екрані має
# з'явитися повідомлення про те, що сума цифр числа 15

input_number = input("Enter number: ")
sum_of_digits = sum(int(symbol) for symbol in input_number)
print(sum_of_digits)
