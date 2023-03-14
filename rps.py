"""0; user input and cleaning, clearing the terminal/UI, writing down the scores/saving-scores, having a working rock paper scissors game, being able ot quit"""
import random, os, time
try:
    with open("rpsSave.txt", "r") as f:
        i = [i for i in f.read().split(" ")]
        w = int(i[0])
        l = int(i[1])
except:
    w = 0
    l = 0

print("Rock Paper Scissors Game:\nyou choose either rock, paper, or scissors by typing either 'r', 'rock', 'p', 'paper'... and so on and so forth")
while True:
    inp = input("Enter your choice here: ")
    if inp[0].lower() == "q":
        print("wtf")
        with open("rpsSave.txt", "w") as f:
            f.write(f"{w} {l}")
        break
    # cleaning up input
    for thing in ['r', 'p', 's']:
        if inp[0].lower() == thing:
            inp = thing
        

    # computer's choice
    com = random.choice(['r', 'p', 's'])
    #initate thinking
    print("computer is thinking")
    time.sleep(3)

    if inp == com:
        print("it's a tie")
    elif (inp == "r" and com == "s") or (inp == "p" and com =="r") or (inp == "s" and com == "p"):
        w += 1 
        print("you won")
    else:
        l += 1
        print("you lost")
    time.sleep(1)
    
    print(f"\n\n\nYour score: {w}\nComp score: {l}\n\n\n")
    time.sleep(3)

    os.system('cls' if os.name=="nt" else 'clear')
    print("Rock Paper Scissors game:\nEnter 'q' to quit, if you want that is\n")
    time.sleep(1)


