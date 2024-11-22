import random 
#import random
import csv
#import csv


class Deck: #class deck

  def __init__(self, file): #init function
    self.file = file #self file
    self.cards, self.card_values = self.fcards() #cards and card values
    self.hand = [] #hand

  def fcards(self): #fcards function
    with open(self.file, 'r') as f: #open file
      lines = f.readlines() #lines

    cards = [line.strip() for line in lines] #cards

    card_values = {
        card[0]: 10 if card[0] in {'J', 'Q', 'K', 'A'} else
        (10 if card[0] == '1' else int(card[0]))
        for card in cards #card values for face cards with no number 
    }

    return cards, card_values #return cards and card values

  def randcards(self, numc=2): #randcards function
    randcard = random.sample(self.cards, numc) #random card
    return randcard #return random card

  def addcard(self, cards): #addcard function
    total = sum(self.card_values[card[0]] for card in cards) #total of the sum of the cards
    return total

  def hit(self): #hit function
    new_card = self.randcards(1)[0] #new card
    self.hand.append(new_card) #append new card to hand
    print(f"You drew a {new_card}.") #prints the card you drew

  def stand(self): #stand function
    pass #pass

class User: #class user
  def __init__(self, username): #init function
    self.username = username #username
    self.wins = 0 #wins
    self.busts = 0 #busts

  def won_game(self): #won game function
    self.wins += 1 #wins + 1

  def lost_game(self): #lost game function
    self.busts += 1 #busts + 1

  def export(self, filename='user_wins.csv'): #export function
    user_exists = False #user exists statement
    rows = [] #rows

    with open(filename, 'r') as file: #open file
      reader = csv.reader(file) #reader
      for row in reader: #for row in reader
        if row[0] == self.username: #if row 0 is equal to username
          user_exists = True #user exists statement
          row[1] = str(self.wins) #row 1 is equal to wins
          row[2] = str(self.busts) #row 2 is equal to busts
        rows.append(row) #append row
    with open(filename, 'w', newline ='') as file: #open file
      writer = csv.writer(file) #writer
      for row in rows: #for row in rows
        writer.writerow(row) #writerow

    if not user_exists: #if user exists
      with open(filename, 'a', newline='') as file: #open file
        writer = csv.writer(file) #writer
        writer.writerow([self.username, self.wins, self.busts]) #writerow
      

  def load(self, filename='user_wins.csv'): #load function
    try: #try
      with open(filename, 'r') as file: #open file
        reader = csv.reader(file) #reader
        for row in reader: #for row in reader
          if row[0] == self.username: #if row 0 is equal to username
            self.wins = int(row[1]) #wins
            self.busts = int(row[2]) #busts
    except FileNotFoundError: #except file not found
      pass #pass

  def stats(self, filename='user_wins.csv'): #stats function
    found_user = False #found user statement

    with open(filename, 'r') as file: #open file
      reader = csv.reader(file) #reader
      for row in reader: #for row in reader
        if row[0] == self.username: #if row 0 is equal to username
          found_user = True #found user statement
          wins = int(row[1]) #wins
          busts = int(row[2]) #busts
          print(f'Username: {self.username}') #prints username
          print(f'Wins: {wins}') #prints wins
          print(f'Busts: {busts}') #prints busts
      if not found_user: #if not found user
        print("User does not Exist.") #prints user does not exist
          


  

    
