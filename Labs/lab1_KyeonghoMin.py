# Kyeongho Min | KMin@scu.edu
# MSIS2607 Data Analytics - Python: Lab 1

import random


# A dictionary of options 
mydict = {"1" : "Fibonacci", "2" : "FizzBuzz", "3" : "Primenum", "4" : "Randomnum", "5" : "Quit"}

# User's first input check & call the option
def runtest():
    firstnum = input("Enter the number(1-5): ")
 
    # User's first input validation check    
    if firstnum.isdigit() == False:     # If input is not a positive integer, go back to the first query
        print("That's not an option.")
        runtest()
    elif int(firstnum) == 5:   # If input is "5", exit the program
        exit()
    elif int(firstnum) not in range(1,5):   # If input is not a number(1-4), go back to the first query
        print("That's not an option.")
        runtest()    
    else:     # Valid first input
        choice = mydict[firstnum]    
        print()
        print("Your choice is: " + choice)
        play(choice)   # Call the function that calls one of options
    
# This function calls the option that user chose
def play(name):
    print()
    secondnum = input("Enter the positive integer: ")
    
    # User's second input validation check
    if secondnum.isdigit() == False:   # If input is not a positive integer, go back to 'second input'
        print("That's not a positive integer")
        play(name)
    else:    # Valid input: Call the function 
        if name == "Fibonacci":
            return fibonacci(int(secondnum))
        if name == "FizzBuzz":
            return fizzbuzz(int(secondnum))
        if name == "Primenum":
            return primenum(int(secondnum))
        if name == "Randomnum":
            return randomnum(int(secondnum))
        
        
    
# Fibonacci function
def fibonacci(n):
    print()
    print("Your Fibonacci sequence is:")
    
    a, b = 0, 1   # The first and second Fibonacci number
    count = 0   
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        for count in range(n):
            print(a)
            c = a + b
            a = b
            b = c
            count += 1  
        
# FizzBuzz function       
def fizzbuzz(n):
    print()
    print("Your FizzBuzz sequence is:")  
    
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
# Prime Number function            
def primenum(n):
    if n == 1:   # Validation check: If input is 1, go back to 'second input' for prime number
        print()
        print("No prime numbers. Select a number larger than 1")
        play("Primenum")
    else:
        print()
        print("The prime numbers up to your number are:")
        for i in range(1,n+1):
            count = 0
            for num in range(2, (i//2 +1)):
                if(i % num == 0):
                    count += 1
                    break
            if(count == 0 and i != 1):
                print(i)
                
# Random number function                
def randomnum(n):
    mylist = [random.randrange(-50, 51, 1) for i in range(n)]
    
    print()
    print("Your random numbers are:")
    print(mylist)
        
    
            
# Main function: Start the execution of the program       
if __name__ == "__main__":
    while(1):
        print()
        print("---Let's start a game!---")
        for key in mydict:
            print(key,mydict[key])   # print 'mydict' dictionary for user to choose option
        runtest()   # Call the runtest function to start a game
    