''' Problem 3 '''
#Set the global variable
number = 0
result = 0

#Define the main function
def main():
    inputValidation() #Call the inputValidation function
    factorial() #Call the factorial function

#Define inputValidation function
def inputValidation():
    global number #Use the global variable
    while True: #Repeat until a valid input is obtained
        try:
            num = int(input("Enter a number for calculating the factorial: "))
            number = num
            if num < 0: #If number is negative, print an error message.
                print("Please enter a nonnegative integer.")
            else: #If the input is valid, assign it to the global variable and exit the loop
                return num
        except ValueError: # If the input cannot be converted to an integer, print an error message
            print("Invalid input. Please enter a nonnegative integer.")

#Define factorial function
def factorial():
    global result #Use the global variables
    global number
    result = 1 #Initialize the factorial result.
    for i in range(1, number + 1):
        result *= i # Multiply the result by each number from 1 to 'number'
    print(f'The factorial of {number} is {result}')

# Execute the main function
main()
