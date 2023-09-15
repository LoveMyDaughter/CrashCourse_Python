# 220 Написати overload методи Add які в залежності від параметрів або додають
# цифрові значення, або об'єднують введені тексти.
# ? Передбачити аргументи за замовчуванням і використання статичних полів\методів

class Couple:

    amount_of_runs = 0
    amount_of_nums_additions = 0
    amount_of_str_concatinations = 0

    @classmethod
    def add(cls, a=0, b=0):
        cls.amount_of_runs += 1
        if isinstance(a, int) and isinstance(b, int):
            cls.amount_of_nums_additions += 1
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            cls.amount_of_str_concatinations += 1
            return a + b
        else:
            raise ValueError

    @classmethod    
    def counting(cls):
        return (
            f"amount_of_runs: {cls.amount_of_runs}\n"
            f"amount_of_nums_additions: {cls.amount_of_nums_additions}\n"
            f"amount_of_str_concatinations: {cls.amount_of_str_concatinations}\n"
        )
              


pair_1 = Couple()
pair_2 = Couple()

pair_2.add(3, 5)
pair_1.add(1, 2)
pair_2.add("Name", "Lastname")

print(pair_1.counting())
