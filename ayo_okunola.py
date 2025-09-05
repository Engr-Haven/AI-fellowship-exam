#Question 1 >>>
#x = int(input())
#y = int(input())

#def calc():
 #   if x == int(input()):
  #      print()


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
