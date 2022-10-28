# Write program to handle all user error
'''Follow this requirements:
1. Ask user to enter 2 numbers
2. Ask user to choose an operation: +, -, /, *
3. Perform the operation in a try-except block
4. Print the result or the error if there is any
5. Ask user if they want to continue
6. If yes, repeat the process
7. If no, exit the program
'''

# You should write your code by using funtions naja

# Ask user to enter 2 numbers


def get_input():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2
# Ask user to choose an operation: +, -, /, *


def get_operation():
    operation = input("Enter the operation: ")
    return operation
# Perform the operation in a try-except block


def perform_operation(num1, num2, operation):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Invalid operation"
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid number")
    except:
        print("Something went wrong")
# Print the result or the error if there is any


def printresult(result):
    print(result)
# Ask user if they want to continue


def continue_program():
    continue_program = input("Do you want to continue? (y/n): ")
    return continue_program
# If yes, repeat the process


def repeat():
    num1, num2 = get_input()
    operation = get_operation()
    result = perform_operation(num1, num2, operation)
    printresult(result)
    continue_prog = continue_program()
    if continue_prog == 'y':
        repeat()
    else:
        print("Thank you for using our program")
# If no, exit the program


def main():
    repeat()


if __name__ == '__main__':
    main()
