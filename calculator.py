"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

operation = input("Enter your operation: ")
operation_list = operation.split(' ')
print(operation_list)

if operation_list[0] == 'add' or operation_list[0] == '+':
    addition_result = add(int(operation_list[1]), int(operation_list[2]))
    print(addition_result)