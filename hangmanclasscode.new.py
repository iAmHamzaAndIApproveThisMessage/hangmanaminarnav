from __future__ import print_function

word = ""
letter = ""
updatedSpaces = []
lives = 6

def initialize():
    word = "earring"
    print['_ _ _ _ _ _ _']

def getLetter():
    print('Guess a letter.')
    letter = raw_input()
    global letter
    
def won():
    if letter in word:
        print('Yay, you won!!') 
    if letter not in word:
        print(getLetter)      
        
          
                         
def main():
    initialize()
    getLetter()
    check(letter)                



bupdatedSpaces=['-','-','-','-','-']
word='steve'
lives=5
def check(letter):
    global lives
    global updatedSpaces
    global word
    if letter in word:
        for i in range(0,len(word)-1):
            Hamza=word.find(letter, i, len(word))
            if Hamza != -1:
                updatedSpaces[Hamza]=letter
    else:
        lives=lives-1
        print('Not in word,', lives, 'lives left!')
    print(updatedSpaces)

main()