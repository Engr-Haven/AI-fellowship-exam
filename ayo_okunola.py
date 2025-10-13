
#Question 1 >>>

def calc():
    operator = input("Enter an operator (+, -, *, /) or type 'exit' to quit: ")
   
    if operator == "exit":
        print("Thank you for using the calculator.")
        return
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        outcome = num1 + num2
        print(f"The result of {num1} + {num2} is {outcome}")
    elif operator == "-":
        outcome = num1 - num2
        print(f"The result of {num1} - {num2} is {outcome}")
    elif operator == "*":
        outcome = num1 * num2
        print(f"The result of {num1} * {num2} is {outcome}")
    elif operator == "/":
        outcome = num1 / num2
        print(f"The result of {num1} / {num2} is {outcome}")
    else:
        print(f"{operator} is not a valid operator.")

calc()

#Question 2 >>>

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int((user_input))   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


#Question 3 >>>

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
