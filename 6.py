a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

if a + b > c and a + c > b and b + c > a:
    # Визначення типу трикутника
    if a == b == c:
        print("Рівносторонній трикутник")
    elif a == b or a == c or b == c:
        print("Рівнобедрений трикутник")
    else:
        print("Різносторонній трикутник")
else:
    print("Трикутник не існує")