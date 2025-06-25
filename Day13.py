# --------------------------------------------
# Day 13 - Debugging 🐞🧠
# --------------------------------------------
# This day focuses on techniques like:
# - Describing the problem
# - Reproducing the bug
# - Playing computer (manually tracing logic)
# - Using print() to expose values
# - Spotting red underlines (syntax bugs)
# - Assignment vs comparison bugs
# - Loop logic issues

# --------------------------------------------
# 🧩 1. Describe the Problem
# --------------------------------------------

# ❌ Bugged:
def my_function():
    for i in range(1, 20):  # Loops from 1 to 19
        if i == 20:
            print("You got it")
my_function()

# ✅ Fixed:
def my_function():
    for i in range(1, 21):  # Now includes 20
        if i == 20:
            print("You got it")
my_function()


# --------------------------------------------
# 🧩 2. Reproduce the Bug
# --------------------------------------------

# ❌ Bugged:
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])  # IndexError if dice_num == 6

# ✅ Fixed:
dice_num = randint(1, 6)
print(dice_images[dice_num - 1])  # Adjust for 0-based indexing


# --------------------------------------------
# 🧩 3. Play Computer (Trace Each Line)
# --------------------------------------------

# ❌ Bugged:
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1996:
    print("You are a millennial.")
elif year > 1996:
    print("You are a Gen Z.")

# ✅ Fixed:
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1996:
    print("You are a millennial.")
elif year > 1996:
    print("You are a Gen Z.")
else:
    print("You might be Gen X or a Boomer.")


# --------------------------------------------
# 🧩 4. See Red Underlines / Fix Syntax Errors
# --------------------------------------------

# ❌ Bugged:
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")  # Indentation error + no f-string

# ✅ Fixed:
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid number. Please enter a number.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")


# --------------------------------------------
# 🧩 5. Assignment vs Comparison
# --------------------------------------------

# ❌ Bugged:
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))  # Used == instead of =
total_words = pages * word_per_page
print(total_words)

# ✅ Fixed:
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)


# --------------------------------------------
# 🧩 6. Use print() to Expose Hidden Values
# --------------------------------------------

# 💬 print() is your friend. It can help expose hidden values while your code is running.
# In a for loop, it's difficult to see intermediate values — so use print() to track what's happening.

def calculate_total_words(pages):
    total_words = 0
    for word_per_page in pages:
        print(f"Processing: {word_per_page}")  # Debug print
        total_words += word_per_page
    return total_words

print(calculate_total_words([100, 200, 150]))  # Example output: 450


# --------------------------------------------
# 🧩 7. Debugging List Append Inside Loop
# --------------------------------------------

# ❌ Bugged:
import random
def add(n1, n2):
    return n1 + n2

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
    b_list.append(new_item)  # ❌ Only appends once
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# ✅ Fixed:
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
        b_list.append(new_item)  # ✅ Correct placement
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
