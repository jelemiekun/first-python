first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

operation_dialogue = """
Select operation:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Modulus
6 - Exponent
"""
print(operation_dialogue)
operation_selected = int(input("Choose operation: "))

result = 0
result = float(result)

match operation_selected:
    case 1:
        result = first_number + second_number
    case 2:
        result = first_number - second_number
    case 3:
        result = first_number * second_number
    case 4:
        result = first_number / second_number
    case 5:
        result = first_number % second_number
    case 6:
        result = first_number ** second_number

print(f"Result: {result}")
