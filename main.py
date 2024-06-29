# Task 1
name = input("Name")
print(f"Hello, {name}!")
# Task 2
a = int(input("Ввести перше число: "))
b = int(input("Ввести друге число: "))
c = int(input("Ввести третє число: "))
d = int(input("Ввести четверте число: "))
e = int(input("Ввести п'яте число: "))
print("Максимальне значення:", max(a, b, c, d, e))
print("Мінімальне значення:", min(a, b, c, d, e))
average = (a + b + c + d + e) / 5
print("Середнє значення:", average)
# Task 3
a = input("Вести перше число: ")
b = input("Вести друге число: ")
a = int(a)
b = int(b)
c = a + b
print(f"Сума: {c}")
d = a - b
print(f"Різниця: {d}")
e = a * b
print(f"Множення: {e}")
i = a / b
print(f"Ділення: {i}")
l = a // b
print(f"Ціле-чисельне ділення: {l}")
# Task 4
r = input("Вказати радіус кола: ")
r = int(r)
d = r * 2
print(f"Діаметр ркружності: {d}")
b =  d * 3.14
print(f"Довжина окружності: {b}")
s = 3.14 * (r ** 2)
print(f"Площина окружнсті: {s}")
# Task 5
p = 1000
r = 0.10
n = 10
print(f"10 років: {p * (1 + r) ** n}")
u = 20
print(f"20 років: {p * (1 + r) ** u}")
o = 30
print(f"30 років: {p * (1 + r) ** o}")
# Task 6
d = 40.1
a = float(input("Гривня: "))
print(f"Долари: {a * d}")
# Task 7
number = input("Введіть тризначне число: ")
print(number[0])
print(number[1])
print(number[2])
name = input("name")
print(f" Hi, {name}")