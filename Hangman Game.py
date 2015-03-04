#Python assignment 3
#program for HANGMAN game

import random #importing random for random.randint() function
outercontrol=-1
while outercontrol==-1: #outer-loop for running the program based on condition
    #creating dictionary for the words used in the game
    dictionary = {'Sports':['Ronaldo','Messi','Rooney','Jordan','Football'],'Country':['Singapore','India','China','Nigeria','Uganda'],'City':['London','Texas','Mumbai','Sydney','Moscow'],'Items':{'Scissors','Pencil','Eraser','Scale','Table'}} 
    y = random.randint(0,4) # generating a random number between 0 and 4 including both the numbers
    #options of questions for the user
    print("1.Country")
    print("2.Sports")
    print("3.City")
    print("4.Items")
    choicenum = int(input("Enter the choice number: ")) #accepting the choice for the category
    country = [value for value in dictionary['Country']]
    sports = [value for value in dictionary['Sports']]
    city = [value for value in dictionary['City']]
    items = [value for value in dictionary['Items']]
    #assigning numbers to specific category
    if(choicenum==1):
        word = country[y]   
    elif(choicenum==2):
        word = sports[y]
    elif(choicenum==3):
        word = city[y]
    elif(choicenum==4):
        word = items[y]
    else:
        print("Invalid Choice!! Program terminates")
        break
    word= word.lower() #converting word to lower-case 
    wordlist = list(word) # to split the words as letters in a list
    wordlength = len(word) # to fid the length of the word in the game
    count = i = 0; # temporary variables used in program execution
    misses=[] #list for storing the misses 
    k = ['_' for i in range(wordlength)]
    attempts = 6 #total number of attempts
    while count<=wordlength:
        for t in k:
            print(t,end=' ')
        print(" ")
        guess = input("Guess: ") # accepting guess from the user
        guess.lower()       #converting guess to lower case
        print("Misses: ",end='')    #display elements in misses list
        for o in misses:
            print(o,end=' ')
        print(" ")          #printing space
        l = x = 0           #temporary variables
        for x in range(0,wordlength):
            if(wordlist[x] == guess):
                l+=1
                if k[x]==guess:     #condition to check if the element has already been entered by the user
                    break
                else:
                    k[x] = guess;   #gets executed if the letter is entered for first time by the user
                    count+=1        #increment counter variable to keep track of the number of letters discovered
   
        if(l==0):
            misses.append(guess) #to append misses if the guess letter is not found in the word
            attempts-=1         #decrement attempts if the guess is wrong
        if(count==wordlength):  #condition for player win
            print("YOU WIN")
            print("The word is: ",word)
            break;
        if(attempts==0):        #condition for game over
            print("GAME OVER")
            print("The word is: ",word)
            break;
        else:
            print("Number of attempts left: ",attempts) #display number of attempts left
    variable_check = str(input("Do you want to continue?(y/n): "))
    if(variable_check=='y'):
        outercontrol=-1
    else:
        break
    
    
