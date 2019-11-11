def summation(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def sum_vector(x):
    sum = x[0]
    for i in range(1,len(x)):
        sum = summation(sum, x[i])
    return sum

def average(x):
    return sum_vector(x) / len(x)

def input_base(usevar, z):
    if usevar == "y":
        x = z
        y = float(input("Enter the second number: "))
    else:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
    return x, y

def input_vector():
    n = int(input("Enter the length of your vector: "))
    x = input("Input the vector (separated by space): ")
    x = x.split(" ")
    x = [float(x[i]) for i in range(len(x))]
    return x

def main():
    print("Choose one operation you want to do!")
    print("1. Summation\n2. Subtraction\n3. Multiplication\n4. Division\n5. Vector Summation\n6. Average")
    z = None
    while True:
        print()
        code = int(input("Enter the operation code: "))

        if "cont" in locals() and code in range(1,5):
            usevar = input("do you want to use the previous result (y/n)? ")
        else:
            usevar = None

        if code == 1:
            x, y = input_base(usevar, z)
            z = summation(x, y)
        elif code == 2:
            x, y = input_base(usevar, z)
            z = subtraction(x, y)
        elif code == 3:
            x, y = input_base(usevar, z)
            z = multiplication(x, y)
        elif code == 4:
            x, y = input_base(usevar, z)
            z = division(x, y)
        elif code == 5:
            x = input_vector()
            z = sum_vector(x)
        elif code == 6:
            x = input_vector()
            z = average(x)

        print("Result: ", z)

        cont = input("Do you want to continue (y/n)? ")
        if cont == "y":
            continue
        elif cont == "n":
            break

main()