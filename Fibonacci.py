#This program asks the user how many components of the Fibonacci sequence he/she would like printed
#and prints them

# 1 1 2 3 5 8 13 21 34 55 etc.

numbers_generated = int(input("How many Fibonacci numbers would you like to print today?  ")) #be sure to turn input to integer

def fibonacci(numbers_generated): #our function that creates and prints the fibonacci sequence to a certain length.
#cannot compute the sequence to infinity or program will not reach next line of code.
    sequence = [1,1,2,3,5] #just a nice start
    next_number = 0 #initialization
    while len(sequence) <= numbers_generated: #tells when to stop computing the sequence
        next_number = (sequence[-1] + sequence[-2]) #computes next number
        sequence.append(next_number) #adds next number
    print(sequence[0:numbers_generated]) #prints sequence up until necessary.

fibonacci(numbers_generated) #calls the function to print the user's desired number of components of the Fibonacci 
