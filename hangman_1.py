import random
word_list = [
    "shah rukh khan", "salman khan", "amitabh bachchan", "aamir khan",
    "ranbir kapoor", "ranveer singh", "akshay kumar", "deepika padukone",
    "alia bhatt", "priyanka chopra",
    "narendra modi", "rahul gandhi", "arvind kejriwal", "yogi adityanath",
    "sachin tendulkar", "virat kohli", "ms dhoni", "rohit sharma",
    "kapil dev", "sunil gavaskar",
    "elon musk", "bill gates", "steve jobs", "mark zuckerberg",
    "jeff bezos", "barack obama", "donald trump", "joe biden",
    "vladimir putin", "xi jinping",
    "leonardo dicaprio", "brad pitt", "tom cruise", "johnny depp",
    "robert downey jr", "chris evans", "chris hemsworth",
    "scarlett johansson", "emma watson", "keanu reeves",
    "cristiano ronaldo","richa tiwary", "lionel messi", "neymar",
    "serena williams", "roger federer", "rafael nadal",
    "lewis hamilton", "michael jordan", "kobe bryant", "usain bolt",
    "walter white", "harry potter", "hermione granger", "ron weasley",
    "iron man", "captain america", "thor", "loki",
    "bruce wayne", "joker", "superman", "spider man",
    "luke skywalker", "sherlock holmes", "thomas shelby",
    "homelander", "max verstappen"
]

def printhangman(l):
    if l == 6:
        print(" _ _ _ _") 
        print("|       |")
        print("|       |")
        print("|    ")
        print("|    ")
        print("|       ")
        print("|      ")
        print("|    ")
        print("|      ")
        print("|     ")
        print("|     ")
        print("|               ")
        print("|_ _ _ _ _ _ _  ") 
    elif l==5:
        print(" _ _ _ _") 
        print("|       |")
        print("|       |")
        print("|    (o   o)")
        print("|    (  _  )")
        print("|        ")
        print("|     ")
        print("|     ")
        print("|       ")
        print("|       ")
        print("|     ")
        print("|               ")
        print("|_ _ _ _ _ _ _  ") 
    elif l==4: 
        print(" _ _ _ _") 
        print("|       |")
        print("|       |")
        print("|    (o   o)")
        print("|    (  _  )")
        print("|       |   ")
        print("|       |  ")
        print("|       |   ")
        print("|       |   ")
        print("|    ")
        print("|   ")
        print("|               ")
        print("|_ _ _ _ _ _ _  ") 
    elif l==3:
        print(" _ _ _ _") 
        print("|       |")
        print("|       |")
        print("|    (o   o)")
        print("|    (  _  )")
        print("|       |   ")
        print("|     //|  ")
        print("|    // |  ")
        print("|       |   ")
        print("|      ")
        print("|    ")
        print("|               ")
        print("|_ _ _ _ _ _ _  ") 
    elif l==2:
        print(r" _ _ _ _") 
        print(r"|       |")
        print(r"|       |")
        print(r"|    (o   o)")
        print(r"|    (  _  )")
        print(r"|       |   ")
        print(r"|     //|\\  ")
        print(r"|    // | \\ ")
        print(r"|       |   ")
        print(r"|       ")
        print(r"|      ")
        print(r"|               ")
        print(r"|_ _ _ _ _ _ _  ") 
    elif l==1:
        print(r" _ _ _ _") 
        print(r"|       |")
        print(r"|       |")
        print(r"|    (o   o)")
        print(r"|    (  _  )")
        print(r"|       |   ")
        print(r"|     //|\\  ")
        print(r"|    // | \\ ")
        print(r"|       |   ")
        print(r"|     //  ")
        print(r"|    //   ")
        print(r"|               ")
        print(r"|_ _ _ _ _ _ _  ") 
    elif l==0:
        print(r" _ _ _ _") 
        print(r"|       |")
        print(r"|       |")
        print(r"|    (o   o)")
        print(r"|    (  _  )")
        print(r"|       |   ")
        print(r"|     //|\\  ")
        print(r"|    // | \\ ")
        print(r"|       |   ")
        print(r"|     // \\  ")
        print(r"|    //   \\ ")
        print(r"|               ")
        print(r"|_ _ _ _ _ _ _  ")



def game():
    global user_inputs
    global chances 
    global placeholder
    global gamefinish
    if chances!=0 and placeholder!=chosen_word:
        print("word is:", placeholder)
        print("you have",chances,"chances")
        if user_inputs!=[]:
            print("your previous guesses are:", user_inputs)
        i = input("enter your guess letter: ")
        
        check(i)
        printhangman(chances)
        return False
    else:

        if chances == 0:
            print("you lost")
            print("the word was:", chosen_word)
            printhangman(chances)
            gamefinish = 1
            menu(0)

        elif placeholder==chosen_word:
            print("you won!")
            gamefinish = 1
            menu(0)




def check(n):
    global gamefinish 
    global chances 
    global placeholder
    global user_inputs
    if n==chosen_word:
        print("correct guess")
        placeholder = chosen_word
    elif n in user_inputs:
        print("you have already guessed this letter")

    elif n in chosen_word:
        user_inputs.append(n)        
        print("correct guess:")
        placeholder = ""

            
        for i in chosen_word:
            if i == " ":
                placeholder+=" "
            elif i in user_inputs:
                placeholder+=i
            else:
                placeholder+="_"
    else:
        print("incorrect guess")
        chances-=1
    

def menu(z):
    global chosen_word
    global user_inputs
    global chances  
    global gamefinish
    global placeholder
    if z==1:
        m = input("Do you want to play hangman? enter y/yes or n/no : " ).lower()
        
    else:
        m = input("do you want to play again? enter y/yes or n/no : " ).lower()

    if m=="y" or m=="yes":
        
        chosen_word= random.choice(word_list) 
        #global chances
        chances = 6

        #global user_inputs
        user_inputs = []

        #global placeholder
        placeholder = ""
        for i in chosen_word:
            if i == " ":
                placeholder+=" "
            else:
                placeholder+="_"

        gamefinish = 0
            
        while gamefinish != 1:
            game()
    elif m=="n" or m=="no":
        print("OK BYE")
    else:
        print("invalid input")
        menu(1)


menu(1)