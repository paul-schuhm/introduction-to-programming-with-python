LIMIT=1000

number1=None
number2=None

while(True):

    number1=int(input("Enter number1: "))

    if number1 == 0:
        break;

    number2=int(input("Enter number2: "))

    if number1 * number2 < LIMIT:
        print(number1*number2)
    else:
        print(number1+number2)

    #Short notation
    print(f"{number1} is {'Even' if number1 % 2 == 0 else 'Odd'}")
    print(f"{number2} is {'Even' if number2 % 2 == 0 else 'Odd'}")
