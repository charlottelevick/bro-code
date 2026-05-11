# Calculator program
# Practicing input and print statements, operators and if, elif and else functions

operator = input("Please choose an operator (+ - * / %): ")
num1 = float(input("Please choose a number: "))
num2 = float(input("Please choose another number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result), 2)
elif operator == "%":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")