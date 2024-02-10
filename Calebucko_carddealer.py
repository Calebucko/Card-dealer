# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:01:23 2024

@author: Caleben Jahn
"""
import random
NUMCARDS = 52
CardDB = []

DECK = 0
PLAYER = 1
COMPUTER = 2

SUITNAME= ("hearts", "clubs", "spades", "diamonds")
RANKNAME= ("ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
        "ten", "jack", "queen", "king")
HANDS= ("deck", "computer", "player")

def main():
    cardDB= initCards()
    
    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)
        showDB(cardDB)
    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

    
    
def initCards():
    cardDB = []
    for index in range(NUMCARDS):
        cardDB.append(0)
    return cardDB

def assignCard(cardDB, hand):
    cardNum= random.randrange(NUMCARDS) 
    cardDB[cardNum]= hand    
    random.shuffle(cardDB)  
    
        
#I'm not entirely sure if this would work, but from what I read
#the shuffle suffix rearranges the order of the list its given, which
#I think would decrease the chance of something repeating twice if it's
#completely switching the array of the list everytime it sifts through it.                   

def showDB(cardDB):
    for cardnum, location in enumerate(cardDB):
        print(f'{cardnum:3}: {getcardName(cardnum):25} {location}')
    #from what I can tell, :3 and :25 are slices? They make the indices of the list
    #and everything line up which is pretty cool. I can assure you I did not use 
    #the magic google to figure this out, don't you worry.
        
        
def showHand(cardDB, hand):
    print(f'Cards dealt to {HANDS[hand]}')
    for cardnum, location in enumerate(cardDB):
        if location == hand:
            print(f'{getcardName(cardnum)}')
            print()

def getcardName(cardnum):
    suit = cardnum // 13
    rank = cardnum % 13 #modulus woaaaaahhhh
    cardName = f'{RANKNAME[rank]} of {SUITNAME[suit]}'
    return cardName

main()