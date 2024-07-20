while True:
    choice = input("Choose Operator..+, -, *, / or Q or q")
    if choice=="Q" or choice=="q":
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice =="+":
        print(num1+num2)
    elif choice=="-":
        print(num1-num2)
    elif choice=="*":
        print(num1*num2)
    elif choice == "/":
        print(num1 / num2)
    else:
        print("Invalid choice...")

