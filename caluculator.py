# creating a caluculator project whilw using os module and functions and contril statements....
import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
opration_dict ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide 
}
def caluculator():
    first_num = int(input("enter first number : "))
    for symbol in opration_dict:
        print(symbol)
    caluculation = True
    while caluculation:
        option_symbol = input("enter an operation : ")
        second_num = int(input("enter second number :"))
        caluculator_function = opration_dict[option_symbol]
        output = caluculator_function(first_num,second_num)
        print(f"{first_num}{option_symbol}{second_num}={output}")
        choice = input(f"enter 'y' to continue caluclation with {output} or 'n' to start a new caluclation or  'x' to exit: "  ).lower()
        if choice == 'y':
            first_num= output
        elif choice == 'n':
            os.system('cls')
            first_num =int(input("enter first number : "))
        else:
            caluculation= False
            print("bye")
caluculator()
# completed...





