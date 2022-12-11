import random
# import time


ls = ["APPLE","ABLE","ANTIENT","ABUSE","ABOUT","ABOVE","ABSENCE","ACCESS","ACCOUNT","ACID","ACROSS","ACT",
    "ACTOR","ACTUAL","ADAPT","ADJUST","ADMIT","ADOPT","AFTER","AFFORD","AGAIN","AGE","AGENT","AGREE","AHEAD",
    "AIM","ALIVE","ALLOW","ALMOST","ALONE","ALONG","ALSO","ALWAYS","AMONG","AMOUNT","ANALYZE","ANGLE","ANIMAL",
    "ANSWER","ANY","APART","APPEAL","APPEAR","APPLY","AREA","ARGUE","ARISE","AROUND","ARRANGE","ARREST",
    "ART","AKS","ATTACK","AUTO","AVOID","AWARD","AWARE","AWAY","BABY","BACK","BAD","BAG","BAKE","BALANCE",
    "BAN","BAND","BANK","BASE","BARRIER","BASIC","BASKET","BATTERY","BATTLE","BEACH","BEAR","BEAT","BECAUSE",
    "BEFORE","BEGIN","BEHIND","BELIEF","BELONG","BELOW","BENEFIT","BEST","BIKE","BIND","BIRD","BIRTH","BLACK",
    "BLAME","BLANKET","BLIND","BLOCK","BOARD","BOAT","BODY","BOOK","BORDER","BORROW","BOTHER","BOTTLE","BOTTOM",
    "BRAIN","BREATH","BUDGET","BUILD","BULLET","BUSY","BUTTON","BOYFRIEND","BUTTER","CABIN","CABLE","CAKE","CALCULATE",
    "CAMERA","CAMPUS","CANCER","CANDIDATE","CAPABILITY","CAPTAIN","CAR","CARBON","CARD","CARRER","CAREFUL","CARRY","CASE","CASH",
    "CAT","CATCH","CAUSE","CEILING","CELEBRITY","CENTER","CHAIN","CHAIR","CHALLENGE","CHAMBER","CHANGE","CHARITY","CHASE",
    "CHEAP","CHECK","CHILD","CHIP","CIRCLE","CITY","CLAIM","ANSHIKA","NIKHIL","SHIVAM","MANASVI","HIMANSHU","RATAN"]



def choice():
    x = random.choice(ls)
    return x


# def jumble(word):
#     y = random.sample(word, len(word))
#     jumbled = "".join(y)
#     return jumbled
def jumble(w):
    ls=[]
    run = True
    word = ""
    while run:
        while True:
            x = random.randint(0,len(w)-1)
            if x not in ls:
                ls.append(x)
            if len(ls) == len(w):
                break
            
        word = ""
        for i in ls:
            word+=w[i]+" "
        if word != w:
            run=False
    # print(ls)
    return word

def play():
    player1=input("Enter your name: ").upper()
#     player2=input("Enter your name: ")
    score = 0
    hint=[]
    for i in range(5):
    # while True:
        pick_word = choice()
        a1 = jumble(pick_word)
        if a1 in ls:
            a1 = jumble(pick_word)
        else:
            print()
            print("The jumbled word is:")
            print(a1)
            print()
        print("Type 'HINT' for hint or 'PRESS ANY KEY' for guess:")
        hn=input().upper()
        if(hn=="HINT"):
            y=random.randint(0,len(pick_word)-1)
            hint.append("* "*(y))
            hint.append(pick_word[y])
            hint.append("* "*((len(pick_word)-1)-y))
            score-=0.5

            print(*hint)
            hint=[]
        else:
            pass
        a = input("Enter the word you are thinking of:\n").upper()
        # time.sleep(5)
        # print("write 'HINT' for hint!")
        if a in ls:
            score += 1
            print()
            print("Yeah! You guessed right")
            print()
        else:
            print()
            print("Better luck next time!")
            print()
            print("The correct word is")
            print(pick_word)
            print()
    print(player1,"Your score is:", score,"out of 5.")
#     print(player2,"Your score is:", score)
    
play()
