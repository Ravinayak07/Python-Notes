import random
import time
name = input("Enter your name :-") 
print("%s Welcome to My Game"%name) 
words = ['kaleen', 'munna', 'guddu', 'bablu',  
         'sweety', 'makbool', 'sardarji', 'gaitonde',  
         'gajgamini', 'beena',]  
word = random.choice(words)
print("Loading......")
time.sleep(3)
print("Lets start the game")
print("Game Theme:-Characters of Mirzapur and Sacred Games")
print("Start Guessing these * letters to win")
letters= ''  
turns = 5
while turns > 0:  
    misses = 0 
    for char in word:   
        if char in letters:  
            print(char) 
        else:  
            print("*")  
            misses=misses+1
    if misses == 0:  
        print("You Win")  
        print("The word is: ", word)  
        break
    letter = input("Guess the letter:")  
    letters=letters+letter 
    if letter not in word: 
        turns -= 1
        print("Wrong input") 
        print("Turns left= ", + turns) 
        if turns == 0: 
            print("You are a looser") 