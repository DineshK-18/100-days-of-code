import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters=int(input("Enter the number of letters:"))
nr_numbers=int(input("Enter the number of numbers:"))
nr_symbols=int(input("Enter the number of symbols:"))
password_list=[]
for char in range(0, nr_letters):
    random_letter = random.choice(letters)
    password_list+=random_letter
for char in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password_list+=random_number
for char in range(0, nr_symbols):
    random_symbol= random.choice(symbols)
    password_list+=random_symbol
print(password_list)
random.shuffle(password_list)
print(password_list)
password=''
for char in password_list:
    password+=char
print(password)