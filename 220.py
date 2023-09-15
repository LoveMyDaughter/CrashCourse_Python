# 220 Написати overload методи Add які в залежності від параметрів або додають
# цифрові значення, або об'єднують введені тексти.
# ? Передбачити аргументи за замовчуванням і використання статичних полів\методів


  

def add( a=0, b=0):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise ValueError


print(add(3, 5))
print(add(1, 2))
print(add("Name", "Lastname"))
