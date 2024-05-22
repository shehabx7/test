# Word guessing game (hangman)
# ○ A list of words will be hardcoded in your program, out of 
# which the interpreter will
# ○ choose 1 random word.
# ○ The user first must input their names
# ○ Ask the user to guess any alphabet. If the random word 
# contains that alphabet, it
# ○ will be shown as the output(with correct placement)
# ○ Else the program will ask you to guess another alphabet.
# ○ Give 7 turns maximum to guess the complete word

import random

#choose a radom name from names list
def choose_word(names):
    r = random.randrange(0,len(names))
    return names[r]


# takes the randomly choosen name
# start the game and ask the user to guess
def guess(word):
    # variables and flags used in the function
    print("if you want to exit input '0'")
    main_flag = 1 # flag for the outer while to be able to exit the loop at any point
    current_guess = ["-" for x in range(len(word))] # holds the current guess starts with "-" for every char in the name
    word = [x for x in word] # stores right name that is being guessed
    counter = 0 # counter for the user tries
    
    # for c in word:
    #     current_guess.append("-")
    
    # the main loop that defines the game
    # exit when the user input "0" or finish the tries
    while main_flag ==1:
        input_flag = 1 # flag for the inner loop
        
        
        if counter > 7: # exit if the user did 7 tries
            print("Game Over!!")
            break
        
        while input_flag == 1: # inner loop count and input user gues
            char = input("guess!! ")
            counter += 1 # count a try
            
            if char == "0": # change the main loop flag if user input "0"
              main_flag = 0
              break  
              
            # checks if the char is valid
            if len(char) == 1 and char.isalpha():
                char = char.lower()
                break
            else:
                print("Not valid guess!")
                print(f"{7 - counter} trails left")
                print("_" * 20)
                print()
            
        if main_flag != 1: # exit main loop
            break
            
        if char in word: # main check if the char is in the guess word
            
            #checks if the char guessed before
            if char not in current_guess:
                
                #if not guessed before input in the current_guess list
                for i,c in enumerate(word):
                    if char == c:
                        current_guess[i] = c
                print("right guess")
                print("".join(current_guess))
                
                # check if the user guessed all word
                if "".join(current_guess) == "".join(word):
                    print("success")
                    break
            else: 
                print("already guessed")
                print("".join(current_guess))
                
        # wrong guess if not in word list
        else:
            print("wrong guess")
            print("".join(current_guess))
            
        # print statues
        print(f"{7 - counter} trails left")
        print("_" * 20)
        print()
    

# takes a valid guess list from user
def input_guess_list():
    names_flag = 1 # flag for the loop
    while names_flag == 1:
        # input name list wih space and convert it to list
        names = input("input your names list a space between names: ").lower()
        names = names.split(" ")
        
        #clean and check the names every char is char
        for i,n in enumerate(names):
            n = n.strip()
            if n.isalpha():
                names[i] = n # updated striped name if valid
                
                # if this is the last name in the last edit flag to exit the main loop
                if i == len(names) - 1:
                    names_flag = 0
                    print("Here is the final name list: ")
                    for x in names:
                        print(x + " ",end = "")
                    break
            else:
                print(f"{n} is not a valid name input the names again!")
                break
    print()
    return names
        
    
        
    
names_list = input_guess_list()
word = choose_word(names_list)
guess(word)


