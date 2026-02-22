def factorial(num):                     #Defines a function named factorial that takes an argument num
    if num == 0 or num == 1:            #base case
        return 1
    else:
        return num * factorial(num - 1)   #recursive case
    
number = int(input("Enter a number : "))        #takes input from user
result = factorial(number)                      #function call on user input number
print(f"Factorial of {number} is : {result}")   #printing the result