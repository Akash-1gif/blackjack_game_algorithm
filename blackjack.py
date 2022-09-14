import random

cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def score(set_of_cards):
    score_of_cards=0
    for i in set_of_cards:
        if i=='A':
            score_of_cards+=1
        elif i=='2':
            score_of_cards+=2
        elif i=='3':
            score_of_cards+=3
        elif i=='4':
            score_of_cards+=4
        elif i=='5':
            score_of_cards+=5
        elif i=='6':
            score_of_cards+=6
        elif i=='7':
            score_of_cards+=7
        elif i=='8':
            score_of_cards+=8
        elif i=='9':
            score_of_cards+=9
        elif i=='10':
            score_of_cards+=10
        elif i=='J':
            score_of_cards+=10
        elif i=='Q':
            score_of_cards+=10
        elif i=='K':
            score_of_cards+=10
    
    if (('A' in set_of_cards) and (score_of_cards+10<=21)):
        score_of_cards+=10
    return score_of_cards 

def stand(player_cards,computer_cards):
    print(f"player cards={player_cards}")
    player_score=score(player_cards)
    print(f"player score={player_score}")
    if (player_score==21):
        print("Player scored a BLACKJACK")
    print(f"computer cards={computer_cards}")
    computer_score=score(computer_cards)
    print(f"computer score={computer_score}")

    if computer_score<15 and player_score>computer_score:
        while computer_score<player_score:
            print("as computer score is less than 15, it will take cards:")
            computer_cards.append(random.choice(cards))
            computer_score=score(computer_cards)
            print(f"now computer has {computer_cards}")
            if (computer_score>21):
                print("computer has been busted!")
    if (computer_score>21 and player_score>21):
        if (computer_score<player_score):
            return "computer"
        else:
            return "player"       
    elif (computer_score>21 and player_score<=21):
        return "player"
    elif (player_score>21 and computer_score<=21):
        return "computer"
    elif (player_score<computer_score):
        return "computer"
    elif (player_score==computer_score):
        return "draw"
    else:
        return "player"

def game():
    print("WELCOME TO BLACKJACK!")
    print("You will be given a credit of $1000 to play the game")
    cash=1000
    interest=True
    while cash>0 and interest==True:
        while 1:
            bet=int(input("Enter your bet amount: $"))
            if bet>cash:
                print("insufficient balance, check your cash...")
                continue
            else:
                break
        
        p1=random.choice(cards)
        p2=random.choice(cards)
        player_cards=[]
        player_cards.append(p1)
        player_cards.append(p2)
        print("You have the following cards:")
        print(player_cards)
        c1=random.choice(cards)
        c2=random.choice(cards)
        computer_cards=[]
        computer_cards.append(c1)
        print("Computer has the following cards:")
        print(computer_cards)
        print("\n\n")
        decision=input("type 'stand' to play your cards or type 'hit' to take more cards:")
        if decision=='hit':
            hit=True
            while (hit==True):
                p=random.choice(cards)
                player_cards.append(p)
                print("now you have the following cards:")
                print(player_cards)
                player_score=score(player_cards)
                if player_score>21:
                    print("you have been busted!")
                    hit=False
                    break
                i=input("do you want to take another card? Type 'yes' for another card else 'no' :")
                if i=='yes':
                    continue
                else:
                    hit=False
        computer_cards.append(c2)
        winner=stand(player_cards,computer_cards)
        if winner=='player':
            print(f"{winner} won the set")
            cash+=bet
        elif winner=='computer':
            print(f"{winner} won the set")
            cash-=bet
        elif winner=='draw':
            print("set draw")
            cash=cash

        print(f"\n\nYour current credits ${cash}")
        if cash<=0:
            print("You ran out of your credits, GAME OVER")
            interest=False
            break
        else:
            w=input("Do you wish to continue the game: Type 'yes' or 'no' :")
            if w=='yes':
                continue
            elif w=='no':
                print(f"You withdrawn ${cash}")
                if cash>1000:
                    print("congratulations! you made a profit")
                else:
                    print("Sorry, you didn't made any profit...")
                interest=False
                break
            else:
                print("BUG")
                break


    print("\n\n\nGAME OVER")



game()
