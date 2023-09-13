# 208. Відомо, що 1 дюйм дорівнює 2.54 см. Розробити додаток, що переводять
# дюйми в сантиметри і навпаки. Діалог з користувачем реалізувати через систему меню.


INCH_RATE = 2.54
convert_type = input(f"Choose convertion type:\n1: Inch >> Cm\n2: Cm >> Inch\n")
num = float(input("Enter number: "))
 
# if convert_type == '1':
#     print(f"{INCH_RATE * num}")
# elif convert_type == '2':
#     print(f"{num / INCH_RATE}")
# else:
#     print("You should choose 1 or 2")

match convert_type:
    case "1": print(f"{INCH_RATE * num}")
    case "2": print(f"{num / INCH_RATE}")
    case _: print("You should choose convert type 1 or 2")
