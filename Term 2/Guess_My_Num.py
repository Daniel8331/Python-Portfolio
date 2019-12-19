#Guess my number
#Daniel Embley

#Imports
import random 
import tic_tac_toe
#Functions


def get_num_in_range(rmin, rmax):
    while True:
        num = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n{")
        if num.isdigit():
            num = int(num)
            if num >= rmin and num <= rmax:
                return num
        print("Not a good value")

def game(rmin,rmax,maxTrys) :
    print( "Welcome to the Guess my number Game")
    rundum = random.randint(rmin,rmax)
    trys = 0
    guess = get_num_in_range
    trys += 1

    while guess != randum and trys != maxTrys:
        if guess > randum:
            print("Guess Lower")
        else:
            print("Guess Higher")
        guess = get_num_in_range(rmin,rmax)
        trys += 1

        if guess == num:
            print("You guessed it!")
        else:
            print("You lose, the numbe was ", num)

    if guess == randum:
        print("Winner")
    else:
        print("Loser")
    print("Number was ",randnum)

def get_number(message):
    while True:
        x = input(message)
        if x.isdigit():
            x = int(x)
            return x
        print("Not a Number")


def confirm(message):
    while True:
        answer = input(message)
        answer = anser.lower()
        if "y" in answer:
            return True
        elif "n" in answer:
            return False
        print("Not a good option")

def game_menu():
    print("""
            Menu
     Option Menu Press 1
     Play Game Press 2
     Press 4 to play Tic Tac Toe
     Quit Press 3
    """)
    while True:
        option = get_num_in_range(1 , 4)

        if option ==1:
            option_ans()
        if option ==2:
            number_game()
        if option ==3:

           break
        if option ==4:
            tic_tac_toe.game()

def create_data_list(minrange, maxrange):
    listdata = []
    for i in range (minrange, maxrange):
        listdata.append(i)
    print(listdata)
    return listdata



def options():
    while True:
        print("Select your game settings")
        print("Easy Medium or Hard")
        print("""
        Press 1 for Easy
        Press 2 for Medium
        Press 3 for Hard
        Press 4 for Computer To Guess
        Press 5 for Custom
        """)
        global rmin
        global rmax
        global maxTrys
        choice = get_number ("")
        if choice == 1:
            rmin = 1
            rmax = 10
            maxTrys = 5
            break
        elif choice == 2:
            rmin = 1
            rmax = 10
            maxTrys = 3
            break
        elif choice == 3:
            rmin = 1
            rmax = 100
            maxTrys = 10
            break
        elif choice == 4:
            x = get_number ("What do you want the minimum number in range to be")
             

    
game_menu()
