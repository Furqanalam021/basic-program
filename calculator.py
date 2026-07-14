# calculator
user=input("Enter user input(+ - * /): ")
num1=int(input("Enter your first number "))
num2=int(input("Enter your secound number "))
if user == "+":
    result=num1 + num2
    print(result)
elif user == "-":
    result=num1 - num2
    print(result) 
elif user == "*":
    result=num1 * num2
    print(result)
elif user == "/":
    result=num1 / num2
    print(result)