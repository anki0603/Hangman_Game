from random import *
def hangman():
    words_list = ['hello','world','chair','keyboard','college','table','football']
    word = choice(words_list)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                main_word = main_word + " _"
        if main_word == word:
            print(main_word)
            print("Hurray!! You won.")
            break

        print("Guess the word",main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter the valid character !!")
            guess = input()

        if guess not in word:
            turns -= 1

            if turns == 9:
                print("9 turns left!!!")
                print("---------------")
            if turns == 8:
                print("8 turns left!!!")
                print("---------------")
                print("       O       ")
            if turns == 7:
                print("7 turns left!!!")
                print("---------------")
                print("       O       ") 
                print("       |       ")
            if turns == 6:
                print("6 turns left!!!")
                print("---------------")
                print("       O       ") 
                print("       |       ")
                print("      /        ")
            if turns == 5:
                print("5 turns left!!!")
                print("---------------")
                print("       O       ") 
                print("       |       ")
                print("      / \      ")
            if turns == 4:
                print("4 turns left!!!")
                print("---------------")
                print("      \O       ") 
                print("       |       ")
                print("      / \      ")
            if turns == 3:
                print("3 turns left!!!")
                print("---------------")
                print("      \O/      ") 
                print("       |       ")
                print("      / \      ")
            if turns == 2:
                print("2 turns left!!!")
                print("---------------")
                print("      \O/ |    ") 
                print("       |       ")
                print("      / \      ")
            if turns == 1:
                print("only 1 turns left!!! Hangman on his last breath")
                print("---------------")
                print("      \O/_|    ") 
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("You loose!!")
                print("You let a good man die -_-")
                print("---------------")
                print("       O_|     ") 
                print("      /|\      ")
                print("      / \      ")
                break


name = input("Enter your name : ")
print("Welcome to the game",name,"!")
print("~----------------------------------~---------------------------------~".center(80))
print("You have 10 attempts to guess the word.")
hangman()