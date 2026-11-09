#A simple calculator application that performs and records simple calculations
#The calculator application should allow users to perform a calculation or print previous calculations stored in a file called equations.txt (that's write and read file functions)

#If user chooses to perform a calculation:
    #the app should accept 2 numbers, and an operation (+,-,*,/) as inputs from user (this is the exception handling)
    #The answer should be displayed for the user, and the equation and answer should be recorded in equations.txt

#If user chooses to print previous equations from equations.txt, display all previous equations
    #use defensive programming to ensure the program doesn't crash if the file doesn't exist
import math
from pathlib import Path

print("Would you like to a) perform a calculation, or, b) print previous calculations?")
answer=input("Type either 'a' or 'b' :")

#write a function to do the calculation:
def calculation(num_1,num_2,operation):
    """
    Calculate the operation selected
    
    Parameters:
    num_1(int): first number entered by user
    num_2(int): second number eneterd by user
    operation: the mathematical operation enetered by user

    returns:
    int: the answer to the calculation
    """
    if operation== "+" :
        return num_1 + num_2
    elif operation== "-":
        return num_1 - num_2
    elif operation=="x":
        return num_1 * num_2
    else:
        return num_1 / num_2

#perform a calculation chosen:
if answer == "a":
    while True:
            try:
                num_1=int(input("You have chosen to perform a calculation. Please enter your first number:"))
                break
            except ValueError:
                print("That was not a valid entry, please enter a whole integer")
    while True:
                try:
                    num_2=int(input("Please enter your second number:"))
                    break
                except ValueError:
                    print("That was not a valid entry, please enter a whole integer")
    while True:
        try:
            operation=str(input("Please enter the calculation you wish to perform (choose from +, -, x, /):"))
            break
        except ValueError:
            print("That was not a valid entry. Please enter one of these operations: +, -, x, /")
    equation= str(num_1) + operation + str(num_2)
    calc_answer=calculation(num_1,num_2,operation)
    print(f"{num_1} {operation} {num_2}= {calc_answer}")
    output_path=  Path(__file__).with_name("equations.txt")
    with output_path.open("w",encoding="utf-8") as file:
        file.write(f"{equation}={calc_answer}" "\n")
else:
    file_path=Path(__file__).with_name("equations.txt")
    file=None
    try:
        with file_path.open("r",encoding="utf-8") as file:
            equations= file.read() #This returns the file as a string
            print(equations)
    except FileNotFoundError:
        print("File not found, or no previous equations")
    finally:
        if file is not None:
            file.close()