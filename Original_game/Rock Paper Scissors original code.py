"""ROCK PAPER SCISSORS GAME PRACTICE"""
#Make it best 2 out of three matches maybe
import random as ran

def run_game():
  wins_count=0
  losses_count=0
  ties_count=0 
  
  while True: 
    user_choice=str(input("Please choose: R,P, or S:  ")) 
    
    my_list={'R':'Rock','P':'Paper','S':'Scissors'}
    my_entry_list= list(my_list.keys())
    computer_choice= ran.choice(my_entry_list)      

    if user_choice.upper()=='Q':
      print(f"WINS:{wins_count}\nTIES:{ties_count}\nLOSSES:{losses_count}")
      print("Thanks for playing!\n")
      break
    
    if user_choice.upper()!='R'and user_choice.upper()!='S' and user_choice.upper()!='P':
      print("Invalid option. Try again\n") 
    
    else:
      if user_choice.upper()==computer_choice:
        ties_count+=1
        print("\nRock, paper, scissors, shoot!\n")
        print(f"Computer chooses {my_list[computer_choice]}")
        print("TIE\n")      

      elif (user_choice.upper()=='R' and computer_choice== 'P') or 
      (user_choice.upper()=='P' and computer_choice=='S') or 
      (user_choice.upper()=='S' and computer_choice=='R'):
        losses_count+=1
        print("\nRock, paper, scissors, shoot!\n")
        print(f"Computer chooses {my_list[computer_choice]}")
        print("LOSS\n")     

      else: 
        wins_count+=1
        print("\nRock, paper, scissors, shoot!\n")
        print(f"Computer chooses {my_list[computer_choice]}")
        print("WIN\n") 
    

user_choice=str(input("Would you like to play again? Type 'Y' for yes or 'Q' to quit any time.\t"))

print("\n")
if user_choice.upper()=='Y':
  run_game()
elif user_choice.upper()=='Q':
  print("Thanks for playing!\n")
  
else:
  while user_choice.upper()!='Y' and user_choice.upper()!='Q':
    print("Sorry that's not a valid option.\n")
    user_choice=str(input("Would you like to play again? Type 'Y' for yes or 'Q' to quit any time.\t"))
    if user_choice.upper()=='Y':
      run_game()
    else:
      if user_choice.upper()=='Q':
        print("Thanks for playing!\n")
