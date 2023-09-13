# 219. Написати програму, яка знаходить в масиві найменше непарне число
# і показує його на екран.

# input_array = [19, 6, 2, 0, 2, 4, -3, 3, 6]
input_array = [19, 6, 2, 0, 2, 4, 3, 3, 4, 20, 3, 7, 17, 6, 0, 5, 4, 44, 2, 8, 9, 0]

def min_odd(array):
    return min(el for el in array if el % 2 == 1)

print(min_odd(input_array))
