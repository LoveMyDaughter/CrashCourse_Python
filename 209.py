# 209 Розробити програму, яка виводить на екран лінію з символів. Кількість
# символів, який використовувати символ, і яка буде лінія - вертикальна, або
# горизонтальна - вказує користувач.

symbol = input("Enter a symbol: ")
count = int(input("Enter symbols amount: "))
direction = input("Select direction:\n1 - Horizontal\n2 - Vertical\n")

if direction == "1":
    print(f"{symbol * count}")
elif direction == "2":
    for i in range (count):
        print(f"{symbol}")
else:
    print("Direction must be 1 or 2")
