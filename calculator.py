"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

operation = input("Enter your operation: ")
operation_list = operation.split(' ')
print(operation_list)

if len(operation_list) < 3:
    first_num = int(operation_list[1])
    second_num = 0
elif len(operation_list) == 3:
    first_num = int(operation_list[1])
    second_num = int(operation_list[2])

    
if operation_list[0] == 'add' or operation_list[0] == '+':
    result = float(add(first_num, second_num))
elif operation_list[0] == 'subtract' or operation_list[0] == '-':
    result = float(subtract(first_num, second_num))
elif operation_list[0] == 'multiply' or operation_list[0] == '*':
    result = float(multiply(first_num, second_num))
elif operation_list[0] == 'divide' or operation_list[0] == '/':
    result = float(divide(first_num, second_num))
elif operation_list[0] == 'square':
    result = float(square(first_num))
elif operation_list[0] == 'cube':
    result = float(cube(first_num))
elif operation_list[0] == 'pow':
    result = float(pow(first_num, second_num))
elif operation_list[0] == 'mod':
    result = float(mod(first_num, second_num))
print(result)
