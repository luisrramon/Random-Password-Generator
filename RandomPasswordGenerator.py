# import necessary modules
import random
import string

# Greeting
print("Welcome to Password Generator!" + "\n" + "Enjoy!!!")

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

# Combining all data
sum = lower + upper + numbers + symbols

# Main program
while 1:
    length = int(input("Enter the length of password: "))
    count = int(input("Enter the amount passwords you would like: "))
    for x in range(0, count):
        password = ""
        for y in range(0, length):
            password_char = random.choice(sum)
            password = password + password_char
        print("Here is your random password: " + password)
    break
