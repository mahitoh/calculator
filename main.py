def calculator():
    print("simple calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            #Get the users imput
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /)")


            #Perform calculation based on operation

            if operation == '+':
                result = num1 + num2

            elif operation == '-':
                result = num1 - num2
            
            elif operation == '*':
                result = num1 * num2
        
            elif operation == '/':
                if num2 == 0:
                    print("Error: cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            print(f'Result: {num1} {operation} {num2} = {result}')


            # Ask if the user wants to continue

            again = input("Do you want to calculate again: (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter validnumbers.")


# Run the calculator
if __name__ == "__main__":
    calculator()