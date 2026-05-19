

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


if a == 0 or b == 0:
    print("Result:", 0)

else:
    
    negative = False

    if (a < 0 and b > 0) or (a > 0 and b < 0):
        negative = True

    
    if a < 0:
        a = -a

    if b < 0:
        b = -b

    
    result = 0

    
    if a < b:
        smaller = a
        larger = b
    else:
        smaller = b
        larger = a

    count = 0
    while count < smaller:
        result = result + larger
        count = count + 1

    
    if negative:
        result = -result

    print("Result:", result)
