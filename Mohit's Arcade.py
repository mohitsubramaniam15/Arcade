import random
def rps():  # rock paper scissors code
 user_wins = 0
 computer_wins = 0
 options = ["rock", "paper", "scissors", "test"]
 options[0]
 while True:
     user_input = input("Type Rock/ Paper/ Scissors or Q or q to quit: ").lower()
     if user_input == "q":
         break
     if user_input not in options:
         continue
     random_number = random.randint(0, 2)
     # rock: 0, paper: 1, scissors: 2
     computer_pick = options[random_number]
     print("computer picked", computer_pick + ".")

     if user_input == "rock" and computer_pick == "scissors":
         print("You won!")
         user_wins += 1
     elif user_input == "paper" and computer_pick == "rock":
         print("You won!")
         user_wins += 1
     elif user_input == "scissors" and computer_pick == "paper":
         print("You won!")
         user_wins += 1
     elif user_input == computer_pick:
         print("nobody won")
     else:
         print("You lost!")
         computer_wins += 1
 print("You won", user_wins, "times.")
 print("The computer won", computer_wins, "times.")
 print("Goodbye!")


def guess():  # code for guessing game

 top_of_range = input("Type a number: ")
 if top_of_range.isdigit():
     top_of_range = int(top_of_range)
     if top_of_range <= 0:
         print("Please type a number more than zero. ")
 else:
     print("please type a number next time. ")
     quit()
 random_number = random.randint(0, top_of_range)

 guesses = 0
 while True:
     guesses += 1
     user_guess = input("Make a guess: ")
     if user_guess.isdigit():
         user_guess = int(user_guess)
     else:
         print("please type a number next time. ")
         continue
     if user_guess == random_number:
         print("You got it!")
         break
     elif user_guess > random_number:
         print("Wrong guess, you were above the number!")
     else:
         print("Wrong guess, you were below the number!")
 print("You got it in", guesses, "guesses")


def quiz():  # code for quiz
 print("Welcome to my computer quiz!")
 score = 0
 answer = input("What does CPU stand for? ").lower()
 if answer == "central processing unit":
     print("Correct!")
     score += 1
 else:
     print("""Wrong :(
     Pro tip - Try checking the spelling""")
 answer1 = input("What does GPU stand for? ").lower()
 if answer1 == "graphics processing unit":
     print("Correct!")
     score += 1
 else:
     print("""Wrong :(
     Pro tip - Try checking the spelling""")
 answer2 = input("What does RAM stand for? ").lower()
 if answer2 == "random access memory":
     print("Correct!")
     score += 1
 else:
     print("""Wrong :(
     Pro tip - Try checking the spelling""")
 answer3 = input("What does ROM stand for? ").lower()
 if answer3 == "read only memory":
     print("Correct!")
     score += 1
 else:
     print("""Wrong :(
     Pro tip - Try checking the spelling""")
 answer4 = input("What does PSU stand for? ").lower()
 if answer4 == "power supply":
     print("Correct!")
     score += 1
 else:
     print("""Wrong :(
     Pro tip - Try checking the spelling""")
 print("you scored", score, "out of 5")

n = input("Do you want to play games(yes or no)? ").lower()
if n == "yes":
  print("""Welcome to Mohit's Arcade!!
  You may choose from the following games:
  1)Rock paper scissors (Type "r")
  2)guess the number (Type "g")
  3)quiz (Type "q")
  4) OR press "e" to end the games""")
  user = "r"
  while(user=="r" or user=="g" or user=="q"):
      user = input("What game do you want to play?").lower()
      if user == "r":
          rps()
      elif user == "g":
          guess()
      elif user == "q":
          quiz()
      elif user == "e":
          print("Please come back again next time")
          break
elif n == "no":
  print("Come back again next time")
else:
  print("Please type a valid input")

