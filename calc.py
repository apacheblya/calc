num1 = int(input("First number: ")) # Input First number
num2 = int(input("Second number: ")) # Input Second number
value = str(input("+, -, *, /: ")) # Input Operation with number
res = '' # Result

operation = ['+', '-', '*', '/'] # list of operation`s

if operation[0] == value:
    res = num1 + num2
    print("Result: ", res)
elif operation[1] == value:
    res = num1 - num2
    print("Result: ", res)
elif operation[2] == value:
    res = num1 * num2
    print("Result: ", res)
elif operation[3] == value:
    res = num1 / num2
    print("Result: ", res)
else:
    print("Invalid input")