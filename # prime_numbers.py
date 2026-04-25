# prime_numbers.py
# Name: Suhaan Bhanwer
# Date: October 19th 2025
# Description: This code takes a number between 2 and 70, and lists all the prime numbers

# Declarations
# squareroot function
from math import sqrt
# the minimum and maximum values for the user unput
MINIMUM_VALUE = 2
MAXIMUM_VALUE = 70

# Input
# Title for the program
print("*"*57)
print("                   PRIME NUMBER FINDER")
print("*"*57)
# sets the variable not_valid to True
not_valid = True
# variable that holds the prompt, changes depending on error
prompt = "Enter a limit to the prime numbers you want displayed: "
# start of a while loop, verifies whether user input is valid or not, handles invalid inputs approprately
while not_valid == True:
    # takes user input
    user_input = input(prompt)
    # checks the value is a number
    if user_input.isnumeric():
         # if value is a number, store it as an integer
        number = int(user_input)
        # validates if the number is between the minimum and maximum values
        if number < MINIMUM_VALUE or number > MAXIMUM_VALUE:
            # if input is not valid, change input prompt
            prompt = "\nThe value entered must be between 2 and 70. Please try again: "
        else:
            # if input is valid, exit the while loop
            not_valid = False
    else:
        # if value is not a number, change the prompt
        prompt = "\nThe value entered must be a whole number. Please try again: "

# Processing
# Title for the displayed prime numbers
print("*" * 59)
print("                 PRIME NUMBERS UP TO {}".format(number))
print("*" * 59)
# for loop that goes from 2 to the number the user selected
for count in range(2, (number) + 1):
    # declares the is_prime variable to true
    is_prime = True
    # sets the limit variable to the squareroot of the count variable
    limit = int(sqrt(count))
    # nested loop from 2 to the limit + 1
    for divisor in range(2, (limit) + 1):
        # modulus each count value by the divisor value
        if count % divisor == 0:
            # if the modulus is 0, the is_prime variable is set to false
            is_prime = False
    # for all values that the is_prime variable is not false, print that number
    if is_prime == True:
        print("X" * count + ' ' + str(count))
            
# Output
# Pause at the end of the code
input("Please press <Enter> to end program...")