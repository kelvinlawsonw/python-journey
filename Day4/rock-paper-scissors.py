rock = '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             '''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''
scissors ='''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''  
import random
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice == 0:
  print(rock)
elif user_choice == 1:  
  print(paper)
elif user_choice == 2:
  print(scissors)   
else:
  print("Invalid input. Please try again.") 

computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print("Computer chose:")
  print(rock)
elif computer_choice == 1:
    print("Computer chose:")
    print(paper) 
elif computer_choice == 2:
    print("Computer chose:")
    print(scissors) 

if user_choice == computer_choice:
  print("It's a draw!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!") 
elif user_choice == 1 and computer_choice == 0:
  print("You win!")   
elif user_choice == 2 and computer_choice == 1:
  print("You win!")
else:
  print("You lose!")  


