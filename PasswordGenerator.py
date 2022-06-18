import random

# The length of the password
passLength = int(input('Enter an amount of letters and symbols of which your password will contain: '))

# Creating the variable for the password
passWord = ''

# A while loop making sure that the password has the correct length
while len(passWord) < passLength:

    # Generates a random integer ranging from 1 to 4
    n = random.randint(1, 4)

    # Picks a letter if the the random number is either 1 or 2
    if n == 1 or n == 2:

        # Collection of all the letters in the english alphabet (Pretty tedious to type out)
        char = ['a', 'b' , 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
            , 'p', 'q', 'r' , 's', 't' ,'u', 'w', 'x', 'y', 'z']

        # Picks a letter
        r = random.randint(0, len(char) - 1)

        # If the integer from before is a 1, then it converts it to be an uppercase letter and adds it to the password
        if n == 1:
            passWord = passWord + (char[r].upper())
        # If the integer is a 2, then it keeps the letter in lowercase and adds it to the password
        else:
            passWord = passWord + char[r]

    # If the integer was the integer 3, then it picks from a range of symbols and adds it to the password
    if n == 3:
        char = ['!', '?', '@', '#', '$', '%', '€', '&']
        r = random.randint(0, len(char) - 1)
        passWord = passWord + char[r]

    # If the integer was the integer 4, then it adds a number to the password
    if n == 4:
        char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        r = random.randint(0, len(char) - 1)
        passWord = passWord + char[r]


# Signals the start of the password and centers
print('\n' + '#########PASSWORD STARTS#########\n'.center(50))

# Variables needed for splitting the password into rows
remainLength = len(passWord)
multiplier = 0


# Splits the password into a new row after every 50 characters
while remainLength != 0:
    print(passWord[(0 + multiplier*50):(49 + multiplier*50)])
    remainLength -= 50
    multiplier += 1

# Signals the end of the password
print('\n' + '##########PASSWORD ENDS##########'.center(50))

# Command in order to quit the program
if input('\nIf you want to exit press ENTER') == '':
    quit()
