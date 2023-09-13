# 202 - Напишіть програму, яка переводить гривні в $, Є.

dollar_rate = 1 / 37.5
euro_rate = 1 / 41.2
uah = int(input("Input Gryvnias: "))

print(f"Amount in $ = {dollar_rate * uah}")
print(f"Amount in Eur = {euro_rate * uah}")
