#Import random module for making random choices
import random
from time import sleep

#Instructions for the game
def Rules(uname):
    sleep(2)
    print("I am computiee and I will be your opponent in this game. ")
    print("There will be 10 rounds.{}, you have to randomly choose any of the three forms i.e. SNAKE, WATER AND GUN.".format(uname))
    sleep(2)
    print("========================\nRULES : \n========================")
    print("Snake VS Water : Snake drinks the water hence wins.")
    print("Gun VS Snake : Gun will kill the snake, hence a point for gun.")
    print("Water VS Gun : The gun will drown in water, hence water win")
    print("If we both choose the same object, the result will be a draw.")
    print("Options : S- Snake, W- Water, G - Gun")
    print("Invalid choice may drop the round.So, make valid choices")
    print("ALL THE BEST!")

#Play Game here
def Game():
    rounds=10
    player_points = 0 #counts player's score
    computiee_points = 0 #counts computer's score
    draw=0
    # Choices allowed in the game
    objects = ["S", "W", "G"]
    while(rounds!=0):
        print("Snake(S) -- Water(W) -- Gun(G) ")
        rounds-=1
        #Exception handling
        try:
            player = input("Choose your option : ")
        except EOFError as e:
            print("Enter valid choice")

        #Wrong choices handling
        if(player not in ["S", "s", "g", "G", "W", "w"]):
            print("Invalid input! try again")
            continue

        #random.choice() randomly choice objects from objects list
        computiee = random.choice(objects)

        #Conditions and winner of each round based on game rules
        if(computiee.lower()=="s"):
            if(player .lower()=="g"):
                computiee_points+=1
                print("-----Computiee Won!-----")
            elif(player .lower()=="w"):
                player_points+=1
                print("-----You Won!!-----")
            else:
                draw+=1
                print("-----Draw-----")
        elif (computiee.lower()=="g"):
            if (player .lower() == "s"):
                computiee_points += 1
                print("-----Computiee Won!-----")
            elif (player .lower() == "w"):
                player_points += 1
                print("-----You Won!!-----")
            else:
                draw += 1
                print("-----Draw-----")
        else:
            if (player .lower() == "g"):
                computiee_points += 1
                print("-----Computiee Won!-----")
            elif (player .lower() == "s"):
                player_points += 1
                print("-----You Won!!-----")
            else:
                draw+=1
                print("-----Draw-----")
        #No. of rounds left
        print(f"{rounds} Left...")

    #Returns scores of the game
    return [player_points , computiee_points]

#Final results based on scores...
def Results(uname, scores):
    if (scores[0]>scores[1]):
        print("Congratulations! {} won".format(uname))
    elif(scores[1]>scores[0]):
        print("Congratualations! Computiee won")
    else:
        print("It's a draw.Try the game again.")
    print(f"{uname} : {scores[0]}\nComputiee : {scores[1]}")


if __name__ == '__main__':
    uname = input("Please enter your name : ")
    print("Hey {}! Welcome to SNAKE - WATER - GUN GAME".format(uname))
    #Rules
    Rules(uname)
    sleep(3)
    print("************************")
    print("Let's start the game")
    #Play Game
    res = Game()
    print("***************************")
    print("Results : ")
    #Declare results
    Results(uname, res)
    print("***************************")



