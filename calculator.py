a = float(input("Enter first  number: "))
b = float(input("Enter second number: "))
c = input("What action you want them to do? (If you want get to the root of number  enter 'sqrt' : ")

if c == '+':
    print(float(a + b))
if c == '-':
    print(float(a - b))
elif c == '*':
    print(float(a * b))
elif c == '/':
    print(float(a / b))
elif c == "**":
    j = int(input("what number you will use?: "))
    g = int(input("What number raise the degree?: "))
    print(float(j ** g))
elif c == 'sqrt':
    x1 = input("sqrt first number of second?: ")
    if x1 == 'first':
        d = a ** 0.5
        print(d)
    if x1 == 'second':
        f = b ** 0.5
        print(f)