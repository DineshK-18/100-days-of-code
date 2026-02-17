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

### **Day 13 - Debugging** 🐞🔧  
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

### **Day 15 - Coffee Machine** ☕💰  
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

> 🚀 **From Day 16 onward, the projects move into intermediate level** — involving OOP, more complex logic, and real-world problem-solving skills like Turtle graphics, Quiz games, and Snake Game.

---

### **Day 16 - OOP Coffee Machine (Revisited)** ☕🔁  
A refactored version of the Day 15 coffee machine project using **Object-Oriented Programming (OOP)** principles.

**Features:**
- Uses classes: `CoffeeMaker`, `MoneyMachine`, `Menu`, and `MenuItem`  
- Separates concerns: resource management, payment processing, menu operations  
- Accepts user input to select drinks  
- Checks resources before making drinks  
- Handles money collection and returns change  
- Special commands:
  - `report`: Shows current resource levels and money collected  
  - `off`: Turns off the machine

**Files Used:**
- `main.py`: Program logic and interactions  
- `coffee_maker.py`: Manages resources and drink making  
- `money_machine.py`: Handles money processing  
- `menu.py`: Manages menu and available drinks  

---

### **Day 17 - Quiz Game (OOP)** ❓🎮  
A Python quiz game built using Object-Oriented Programming principles.

**Features:**
- Uses classes: `Question` and `QuizBrain`  
- Loads a bank of true/false questions from `question_model.py` and `data.py`  
- Asks each question sequentially and checks the user’s answer  
- Tracks the score and progress  
- Ends when all questions are answered and displays the final score  

**Files Used:**
- `main.py`: Runs the game  
- `question_model.py`: Defines the `Question` class  
- `data.py`: Contains the question data  
- `quiz_brain.py`: Handles game logic (asking questions, checking answers, keeping score)

---

### **Day 18 - Turtle Graphics & Hirst Painting** 🎨🐢  
Exploring Python’s `turtle` graphics library with fun drawing projects.

**What I Did:**
- Practiced drawing shapes, random walk patterns, and spirographs using `turtle`  
- Created a **Hirst-style dot painting** by extracting colors from an image using the `colorgram` library  

**Features:**
- Generates a 10x10 grid of colorful dots (Hirst Painting)  
- Uses random colors extracted from an image  
- Demonstrates loops, randomization, and `turtle` graphics  

**Files Used:**
- `main.py`: Contains turtle drawing logic  
- `colorgram.py`: Used to extract RGB colors from an image  

---

### **Day 19 - Turtle Race Game** 🐢🏁  
A fun game built with Python’s `turtle` library where players bet on which colored turtle will win a race.

**Features:**
- Creates multiple turtles with different colors  
- User places a bet on a turtle by choosing a color  
- Turtles race across the screen with random movement steps  
- Declares the winner and compares with user’s bet  

**Files Used:**
- `main.py`: Turtle race logic

---

### **Day 20 & 21 - Snake Game** 🐍🎮  
The classic Snake Game built using Python’s `turtle` graphics, implemented step by step.

**Features:**
- Creates a snake body using multiple square segments  
- Implements snake movement and continuous motion  
- Snake grows longer when it eats food  
- Randomly generated food items using `food.py`  
- Score tracking and display using `scoreboard.py`  
- Game over when snake collides with wall or itself  
- Uses OOP (`Snake`, `Food`, `Scoreboard` classes) for structure  

**Files Used:**
- `main.py`: Runs the game loop  
- `snake.py`: Snake logic and movement  
- `food.py`: Food generation  
- `scoreboard.py`: Score tracking and display  

---

⚡ By Day 21, the Snake Game is fully functional with movement, growth, food, scoring, and game-over conditions!

---

### **Day 22 - Pong Game** 🏓

A classic Pong game built using Python’s turtle module. The player controls a paddle to bounce the ball against the opponent and keep the rally going.

**Features:**
- Ball moves continuously and bounces off walls and paddles
- Player controls left paddle using keyboard inputs (Up and Down)
- Opponent paddle moves automatically
- Score is tracked for both player and computer
- Uses OOP with Paddle and Ball classes

**Files Used:**
- `main.py`: Runs the game loop and handles game logic
- `paddle.py`: Paddle movement logic
- `ball.py`: Ball movement and collision detection
  `scoreboard.py`: Score display

---

### **Day 23 - Turtle Crossing Game** 🐢🚦

A lane-crossing game where the player guides a turtle across a busy road using Python’s turtle module. The goal is to reach the finish line while avoiding moving cars, with increasing difficulty each level.

**Features:**
- Player moves turtle forward using the Up arrow key
- Cars are generated randomly and move across the screen
- Collision detection ends the game when the turtle hits a car
- Levels increase speed and difficulty as the turtle crosses successfully
- Tracks score based on levels completed
- Uses OOP with Player, CarManager, and Scoreboard classes

**Files Used:**
- `main.py`: Runs the game loop and handles game logic
- `player.py`: Controls player turtle movement and start/finish line logic
- `car_manager.py`: Manages car creation, movement, and speed increase per level
- `scoreboard.py`: Tracks and displays current level, and shows game over

---

### **Day 24 – Mail Merge Project** 📄✉️

A simple automation project that generates personalized letters using Python file handling.

**Features:**
- Reads a template letter from a text file
- Reads multiple names from a separate file
- Replaces the placeholder [name] with each actual name
- Automatically generates and saves personalized letters for every recipient
- Stores the output letters in a dedicated ReadyToSend folder

**Concepts Used:**
- File handling (open, read, write)
- String manipulation (replace, strip)
- Loops
- Directory structure management

**Files Used:**
- `main.py`: Core mail merge logic
- Input/Letters/starting_letter.txt: Template letter
- Input/Names/invited_names.txt: List of recipient names
- Output/ReadyToSend/: Generated personalized letters

---

### Day 25 – U.S. States Game (Pandas + Turtle Graphics)🗺️🐢

An interactive geography game built using Python’s turtle module and pandas for data handling. The player guesses U.S. state names, and correct answers are displayed on a blank U.S. map.

**Features:**
- Displays a blank U.S. map using a .gif image
- Accepts user input through a pop-up text box
- Validates state names using data from a CSV file
- Writes correct state names at their respective coordinates on the map
- Tracks the number of correctly guessed states
- Generates a `states_to_learn.csv` file containing all unguessed states when the user exits

**Files Used:**
- `main.py` – Core game logic and turtle interaction
- `50_states.csv` – Dataset containing U.S. state names with their (x, y) coordinates
- `blank_states_img.gif` – Background image of the blank U.S. map
- `states_to_learn.csv` – Auto-generated file listing unguessed states when the user exits

---


