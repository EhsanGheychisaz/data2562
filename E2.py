a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation: ")
x = 0
y = 0
if c == '*' or c == '/':
    y += 20
elif c == '+' or c == '-':
    y += 10
while a > 0 and b > 0:
    d = 0
    if c == '+':
        d = a+b
    elif c == '-':
        d = a-b
    elif c == '*':
        d = a*b
    elif c == '/':
        d = a/b
    i = int(input(f"{a}{c}{b} = "))
    if d != i:
        print(f"Be more careful! {a} {c} {b} = {d}")
    elif d == i:
        print("Good job!")
        if c == '*' or c == '/':
            x += 20
        elif c == '+' or c =='-':
            x += 10
    a = int(input("Enter first number: "))
    if a < 0:
        break
    b = int(input("Enter second number: "))
    if b < 0 :
        break
    c = input("Enter operation: ")
    if c == '*' or c == '/':
        y += 20
    elif c == '+' or c == '-':
        y += 10
    print(y)
s = (x*100)/y
print(f"Your score is : {s}")

