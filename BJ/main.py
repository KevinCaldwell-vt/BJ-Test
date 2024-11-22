'''
This is a very ghetto blackjack. It uses a deck of cardsin a file of a TXT, and a hand of cards in a list. IT also exports into a CSV file to keep track of users as well as wins and losses. Then in which you can search up players and look at their stats. 
Known Errors: Game asks you to hit or stand after a loss, doesnt count that turn but needed response to end game.
'''

from Classes import *  
#importfrom classes all
import sys 
#import system
import time 
#import time 
from colorama import Fore
#import font colour

def print_slow(str): #function to print slow
  for char in str: #for character in string
    time.sleep(.1) #time to sleep
    sys.stdout.write(char) #start writing 
    sys.stdout.flush() #typing effect
def create_user(username): #create or find username
  user = User(username) 
  user.load() #username load to check
  return user #return if user is found or not
def main(): #main function
  username_lookup = input("\nEnter your Username to find Stats: ") #enter username
  name_lookup = User(username_lookup) #checks username
  name_lookup.load() #loads username
  name_lookup.stats() #prints stats

  
  username = input("Enter your username: ") #enter username to play
  user = create_user(username) #create user if not exist
  deck = Deck('cards.txt') #deck = class deck for cards.txt
  deck.hand = deck.randcards(2) #random card amount 2
    

  
  while True: #while true loop
    print(f"Your hand: {deck.hand}") #prints your hand
    handval = deck.addcard(deck.hand) #adds card to hand
    print(f'Your total: {deck.addcard(deck.hand)}') #prints total
    user_input = input("Hit or stand? ").lower() #asks user to hit or stand

    if user_input == 'hit': #if user input is hit
      deck.hit() #hit function
      total = deck.addcard(deck.hand) #total = addcard function
    elif user_input == 'stand': #if user input is stand
      deck.stand() #stand function
      break #breaks loop
    else:
      print("Please enter hit or stand.") #prints please enter hit or stand

    if handval == 21: #if handval is 21
      print("You got 21! You win!") #prints you got 21 you win
      user.won_game() #user won game function
      user.export() #export function for stats
      break #breaks loop
    elif handval > 21: #if handval is greater than 21
      print(f"Bust! Your total is {handval}. You lose!") #prints bust your total is handval you lose
      user.lost_game() #user lost game function
      user.export() #export function for stats
      break #breaks loop

print_slow(Fore.RED + 'Welcome to Blackjack!') 
main()