import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user_choice = int(input("Enter Your Choice(0, 1 or 2): "))
computer_choice = random.randint(0, 2)
print("Computer Chose:", choices[computer_choice])
print("You Chose:",choices[user_choice])
if user_choice == computer_choice:
    print("It's a Tie!")
elif user_choice == 0 and computer_choice == 2:
    print("Rock beat scissors. You win!")
elif computer_choice == 0 and user_choice == 2:
    print("Rock beat scissors. You lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")



