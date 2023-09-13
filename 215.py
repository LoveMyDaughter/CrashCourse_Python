# 214. Написати програму, яка виводить на екран - наступну фігуру:
# ""*********************                                                                                                                                                                                                        
# *                           *                                                                                                                                                                                                        
# *                           *                                                                                                                                                                                                        
# *                           *                                                                                                                                                                                                        
# *                           *                                                                                                                                                                                                        
# *********************                                                                                                                                                                                                        
# ширина і висота фігури встановлюються користувачем з клавіатури.


width = int(input("Enter the width: "))
heigth = int(input("Enter the heigth: "))

print(f"Width: {width}, Height: {heigth}")
for i in range(heigth):
    if i == 0 or i == heigth-1:
        print("*" * width)
    else:
        if width > 1:
            print("*" + (" " * (width-2)) + "*")
        elif width == 1:
            print("*")
