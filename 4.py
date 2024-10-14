bracket = input("Введіть символ-дужку: ")

# Визначення типу дужки
if bracket == '(' or bracket == ')':
    print("кругла дужка")
elif bracket == '[' or bracket == ']':
    print("квадратна дужка")
elif bracket == '{' or bracket == '}':
    print("фігурна дужка")
elif bracket == '<' or bracket == '>':
    print("кутова дужка")
else:
    print("Невідомий символ")