# 216. Написати програму, яка виводить вміст масиву навпаки.
# Приклад: масив 23 11 6 42 перетворюється в 42 6 11 23."

given_array = [23, 11, 6, 42]
# given_array = [1, 0, 1,23, 11, 12, 6, 42, 0]
final_array = []

for i in range(len(given_array)-1, -1, -1):
    final_array.append(given_array[i])

print(final_array)
