num1 = int(input("number one: "))
num2 = int(input("number two: "))
order = input("Enter instruction:")
order = order.lower()

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
remainder = num1 % num2
floor_div = num1 // num2
square = num1 ** num2

if order == "add":
    print(sum)
if order == "sub":
    print(sub)

if order == "mul":
    print(mul)

if order == "div":
    print(div)

if order == "remainder":
    print(remainder)

if order == "floor_div":
    print(floor_div)

if order == "square":
    print(square)



