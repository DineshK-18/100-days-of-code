# 100 Days of Code - Python Projects  
This repository contains small Python projects I build each day as part of the 100 Days of Code challenge. 💻🔥

---

> 🧑‍💻 **Note:** Days 1 to 15 cover beginner-level Python projects — focused on basics, logic building, and foundational programming skills.

---
### **Day 1 - Band Name Generator** 🎸  
A fun little program that asks for the user's city and favorite pet, then combines them to suggest a creative band name.

---

### **Day 2 - Tip Calculator** 💰  
A simple calculator that helps split a restaurant bill among multiple people, including tip percentage, and calculates how much each person should pay.

---

### **Day 3 - Treasure Island Adventure** 🏝️  
A text-based adventure game where the player navigates through choices to find a hidden treasure. It includes multiple paths, game-over scenarios, and one winning outcome — all guided by user input and fun storytelling.

---

### **Day 4 - Rock Paper Scissors Game** ✊🖐️✌️  
A Python implementation of the classic Rock-Paper-Scissors game where the user plays against the computer. It uses ASCII art to make it visually fun and adds logic to determine the winner.

---

### **Day 5 - Password Generator** 🔐  
A customizable password generator that allows the user to specify how many letters, numbers, and symbols to include. It randomizes the order and prints the final password.

---

### **Day 6 - Reeborg's World & Functions** 🤖  

**Topics Covered:**
- Python functions (`def`)
- Loops with conditionals
- Solving maze in Reeborg’s World

**What I Did:**
- Created `turn_right()` and `jump()` functions  
- Used loops and if-else to guide the robot through a maze  

**What I Learned:**
- Importance of reusable functions  
- Better logic building using conditions and loops  

**Screenshots:**  
Included 5 screenshots showing code and final output in Reeborg’s World.

---

### **Day 7 - Hangman Game** 🎯  
A Python version of the classic Hangman game. The player tries to guess the hidden word by entering letters. Wrong guesses reduce lives, and ASCII art shows the Hangman's progress.

**Files Used:**
- `main.py`: Core game logic  
- `hangman_words.py`: Contains the word list  
- `hangman_art.py`: Contains the hangman stages and game logo (ASCII art)

---

### **Day 8 - Caesar Cipher** 🔁🔐  
A text encryption/decryption tool that shifts letters in the alphabet by a user-defined number.

**Features:**
- Encode and decode messages  
- Handles non-alphabet characters without changing them  
- Supports repeated use until user exits  
- Uses ASCII logo from external module `art.py`

---

### **Day 9 - Secret Auction Program** 🤑  
A console-based secret bidding auction game.

**Features:**
- Accepts multiple bidders and stores their bids  
- Clears the screen between bids (for secrecy)  
- Determines and displays the highest bidder  

**Files Used:**
- `main.py`: Auction logic  
- `art.py`: Contains the ASCII logo

---

### **Day 10 - Calculator** 🧮  
A command-line calculator that performs basic arithmetic operations and allows continuous calculations with previous results.

**Features:**
- Supports addition, subtraction, multiplication, and division  
- Uses functions stored in a dictionary for operation selection  
- Allows user to continue chaining calculations or start over  
- Includes ASCII logo from `art.py`

**Files Used:**
- `main.py`: Calculator logic  
- `art.py`: Contains the calculator logo

---

### **Day 11 - Blackjack Game** ♠️🃏  
A simplified version of the Blackjack card game, played in the terminal against the computer.

**Features:**
- Simulates dealing cards from a standard Blackjack deck  
- Follows game rules (Blackjack check, bust, dealer hits until 17, etc.)  
- Compares player and dealer scores to determine the winner  
- Clears screen and replays on user request  
- Includes ASCII logo from `art.py`

**Files Used:**
- `main.py`: Game logic  
- `art.py`: Contains the Blackjack logo

---

### **Day 12 - Number Guessing Game** 🎯🔢  
A terminal-based number guessing game where the player tries to guess a randomly generated number between 1 and 100.

**Features:**
- Difficulty selection (`easy` or `hard`) affecting number of attempts  
- Random number generation using Python’s `random` module  
- Feedback on whether the guess is too high or too low  
- Displays number of attempts left after each guess  
- Ends the game on a correct guess or when attempts run out  
- Includes ASCII logo from `art.py`

**Files Used:**
- `main.py`: Game logic  
- `art.py`: Contains the game logo

---

### Day 13 - Debugging 🐞🔧  
Today was all about learning how to find and fix bugs in Python code.  
I explored different debugging strategies including:

- Describing and understanding the problem
- Reproducing bugs using test cases and print statements
- Manually tracing logic ("playing computer")
- Fixing syntax and logic errors like:
  - Wrong `range` bounds
  - Off-by-one indexing
  - Assignment vs. comparison operators
  - Indentation mistakes
  - Misplaced append statements in loops

Each example included the bugged code, an explanation, and the fixed version — all in one big debug session!  
This helped sharpen my logic and attention to detail. 🔍

✅ Files:  
- `day13_debugging_examples.py` (contains all bugged + fixed cases with comments)

---

### **Day 14 - Higher Lower Game** 🔼🔽  
A comparison-based game where the player guesses who has more followers between two famous people.

**Features:**
- Randomly selects two accounts from a dataset of celebrities  
- Displays name, description, and country of each account  
- User guesses which one has more followers  
- Keeps score for every correct guess  
- Replaces the losing account each round while continuing the game  
- Ends the game when the user makes a wrong guess  
- Includes ASCII logo and vs art from `art.py`

**Files Used:**
- `main.py`: Game logic  
- `art.py`: Contains game logo and VS art  
- `game_data.py`: Contains the celebrity data

  ---

### **Day 15 - Coffee Machine ☕💰**  
A command-line coffee machine simulator that allows users to order espresso, latte, or cappuccino, simulating ingredient use and payment processing.

**Features:**
- Simulates a coffee machine with resources and drink menu  
- Checks if ingredients are sufficient before proceeding  
- Handles coin input (quarters, dimes, nickels, pennies)  
- Calculates total inserted, gives change if needed  
- Tracks total profit and updates remaining resources  
- Special commands:
  - `report`: Shows current resources and profit  
  - `off`: Shuts down the machine  

**Files Used:**
- `main.py`: Coffee machine logic and drink menu


---

**Stay tuned for more daily projects!** 🚀
