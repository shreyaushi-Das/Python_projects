import random

emojis={'r':'🪨','p':'📜','s':'✂️'}
choices=('r','s','p')

while True:
  user_choice=input('Rock,Paper,Scissors?(r/p/s): ').lower()
  if user_choice not in choices:
    print("invalid choice")
    continue
  
  computer_choice=random.choice(choices)
  print(f"You choose{emojis[user_choice]}")
  print(f"computer choose{emojis[computer_choice]}")
  
  if user_choice==computer_choice:
    print('tie!')
  elif(
    (user_choice=='p' and computer_choice=='r') or
    (user_choice=='r' and computer_choice=='s') or 
    (user_choice=='s' and computer_choice=='p')
    ):
    print('You win!😁')
  else:
    print ("you loose!🥺")

  should=input("continue?(y/n)").lower()
  if should=="n":
    break
