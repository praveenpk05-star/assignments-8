from pip._vendor.distlib.compat import raw_input

ans=True
while ans:
    print ("""
    1.add
    2.subtraction
    3.multiplication
    4.division
    """)

    ans = raw_input("choose option : ")
    if ans == "1":
        print("Enter two numbers: ");
        try:
            num1 = int(input('Number : '))
            num2 = int(input('Number : '))
        except ValueError:
            print('Invalid input, You must enter integer value')
        res = num1 + num2;
        print("Result = ", res);
    if ans == "2":
        print("Enter two numbers: ");
        try:
            num1 = int(input('Number : '))
            num2 = int(input('Number : '))
        except ValueError:
            print('Invalid input, You must enter integer value')
        res = num1 - num2;
        print("Result = ", res);
    if ans == "3":
        print("Enter two numbers: ");
        try:
            num1 = int(input('Number : '))
            num2 = int(input('Number : '))
        except ValueError:
            print('Invalid input, You must enter integer value')
        res = num1 * num2;
        print("Result = ", res);

    if ans == "4":
        print("Enter two numbers: ");
        try:
            num1 = int(input('Number : '))
            num2 = int(input('Number : '))
        except ZeroDivisionError:
            print("You have divided a number by zero, which is not allowed.")
        except ValueError:
            print("invalid input, You must enter integer value")
        res = num1/num2
        print("results:", res);




