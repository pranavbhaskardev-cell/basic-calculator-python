print("=== Basic Calculator ===")

first_num = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
second_num = float(input("Enter second number: "))

result = None

if operator == "+":
    result = first_num + second_num

elif operator == "-":
    result = first_num - second_num

elif operator == "*":
    result = first_num * second_num

elif operator == "/":
    if second_num != 0:
        result = first_num / second_num
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator")

if result is not None:
    print("Result:", result)