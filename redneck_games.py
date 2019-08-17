import random
import time

money = 100

# list of game functions here

def rand_gen(x,y):
    
    generator = random.randint(x, y)
    return generator
    

def deer_flip(generator, guess):
    
    if guess == 'heads':
        answer = 0
    elif guess == 'tails':
        answer = 1
        
    if generator == answer:
        return True
            
    else:
        return False


def wager_result():
    
    wager_result = True
            
    while wager_result:
        
        try:
            wager = int(input("So how good are u?  Enter your bet: "))
            
            if wager > money:
                print(f"{name} you ain't got that much!  You gots ${money}")
                wager_result = True
            else:
                wager_result = False

        except ValueError:
            print(f"You have to use numbers {name}!")
            
                            
    return wager
    
def get_bucks(color, color_generator, num1, num1_generator):
    
    if color == "dead":
        color = 0
    else:
        color = 1
    
    if (color == color_generator) and (num1 == num1_generator):
        return True
    
    else:
        return False

def blink():
    pass
    
def redneck_games():

    games = ['buckshot', 'flip deers', 'smarter n you']
    game_cont = True
    game_warning = ("""
                       *******************************************************************************************************
                       *******************************************************************************************************
                       ********* Disclaimer:  Redneck Games holds no grievance towards Rednecks, Trucks or Deers *************
                       *********** Please use the provided spitoons conveniently located by each casino machine **************
                       ******************** This is a Cash only Casino.  All winnings are paid by Check ********************** 
                       *********************** All firearms must be kept on your person at all times *************************
                       **************************** We aren't responsibile for bounced checks ********************************
                       ***************************** Play Responsibly and Drink Heavily **************************************
                       *******************************************************************************************************
                       *******************************************************************************************************
                       """)
    print(game_warning)
    name = input("Please enter your Redneck Name: ")
    print("")
    name = name.capitalize() + "-jo"
    print(f"{name} we've identified you as a special kinda someone.")
    time.sleep(1)
    print("")
    print("The games at Redneck Casinos will prove that fact.")
    time.sleep(1)
    print("")
    print("So Grab your Beers and Let's get some Deers!")
    time.sleep(2)
    print("")
    print(f"Show'em what you got {name}!")
    print("")
                       
    #loop until game ends
    while game_cont:
        
        user_input = ""
        while user_input not in games:        
            user_input = input("Please choose a game: Buckshot, Flip Deers, Smarter N You: ")
            user_input = user_input.lower()
        
        if user_input == games[0]:
            
            
            color_result = True
            num_result = True
            
            while color_result:
                print("")
                print("")
                print("I hear you're a good shot")
                print("Let's see if you can guess if you will hit or miss that big ol buck!")
                color = input("Please choose a color:  Red or Dead? ")
                color = color.lower()
                
                if color == "red" or color == "dead":
                   color_result = False
                else:
                    color_result = True
            
            while num_result:
                
                try:
                    num1 = int(input("Please choose the shotgun gauge you wanna use: "))
                    if num1 < 1 or num1 > 100:
                        print(f"{name} you gotta enter a number for an appropriate shotgun!")
                        num_result = True
                    else:
                        num_result = False
                except ValueError:
                    print(f"{name} you gotta enter a number for an appropriate shotgun!")
                    time.sleep(1)
                    print("Not one of them foreign guns...")
                    num_result = False
                    
            wager = wager_result()
            
            color_generator = rand_gen(0,1)
            num1_generator = rand_gen(1, 20)
            
            
            if get_bucks(color, color_generator, num1, num1_generator) == True:
                new_balance = wager + money
                print(f"Congratulations {name} you won ${wager}!  Your new balance is ${new_balance}")
            else:
                new_balance = money - wager
                if color_generator == 0:
                    result = 'Dead'
                else:
                    result = 'Red'
                
                print(f"You missed! I'll bet you're seeing {result}!")
                time.sleep(1)
                print(f"You was only {num1_generator} inches away from big ol buck.")
                time.sleep(1)
                print(f"You've got ${new_balance} left.  Can't take it with ya?  Right?")

        if user_input == games[1]:
            flip_guess = True
            
            while flip_guess:
                print("")
                print("")
                print(f"{name} So you know a thing about deers?")
                wager = wager_result()
                print("Let's see if you can tell the front from the back?")
                
                guess = input("Please choose one:  Heads or Tails? ")
                guess = guess.lower()
                                
                generator = rand_gen(0,1)
                deer_flip(generator, guess)
                
                
                if generator == True:
                    new_balance = wager + money
                    print(f"Boy {name} you know your deers!")
                    time.sleep(1)
                    print(f"You won ${wager} your wallet is ${new_balance} fuller!")
                    print("")
                    print("")
                    
                else:
                    new_balance = money - wager
                    print(f"I'm sorry {name} you lost. You lost ${wager} Your new balance is {new_balance}")
                
        if user_input == games[2]:
                            
                
                redneck = True
                
                while redneck:
                    
                    print("This here's a test to see who's smarter.")
                    print("Your buddy says he is.")
                    wager_result()
                    print("I gotta feeling he's wrong.")
                    genius = input("Please complete this sentence :")
                    
                    if genius != ".":
                        wager = money - wager
                        print("Dang it {name}!")
                        time.sleep(1)
                        print("....you were so close!")
                        time.sleep(1)
                        print("Now listen here...")
                        print("you ain't gonna let that ol'boy think he's smarter you...are ya?")
                        print(f"Let's go again....this time it's on the me...you show him {name}")
                        redneck = True
                    else:
                        print("Well I'll be a donkey's daughter!  You figured it out!")
                        time.sleep(2)
                        print("You just wonthe Redneck Grand Prize of $1,000,000")
                        time.sleep(1)
                        print("Take a selfie in front of, this here screen to show your buddy who realy is the 'Smart One'")
                        time.sleep(1)
                        print("You may receive your check....shortly.")
                        print("As one Merican to another...you make us proud.")
                
                
                        
        user_cont = input("Would you like to press your luck?  Y or N: ")
        
        if user_cont.upper() == 'Y':
            if money <= 0:
                print("It appears you're dun spent all your money.  Take your broke butt back to the trailer park")
            else:
                game_cont = True
                
        else:
            game_cont = False
    
        
# call the game

redneck_games()









