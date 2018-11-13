import random
import cmath
import telepot

def handDisp(player):
    h = ''
    for i in player:
        h += i+'\n'
    return h[:-1]

def giveCards(player):
    for i in range(13):
        player.append(deck[i])

    for i in range(13):
        deck.pop(0)

    for suit in ['C','D','H','S']:
        suitCard = []
        import pdb; pdb.set_trace()
        
        for card in player:
            if card[-1].upper() == suit:
                suitCard.append(card)

        arranged = False

        while arranged == False and len(suitCard) > 1:
            for i in range(len(suitCard)-1):
                if cardmap[suitCard[i][:-2]] > cardmap[suitCard[i+1][:-2]]:
                    suitCard[i],suitCard[i+1] = suitCard[i+1],suitCard[i]
                    arranged = False
                else:
                    arranged = True

        suitCard.append('  ')
        player.extend(suitCard)

    for i in range(13):
        player.pop(0)

def getPartner(card):
    for i in order:
        if card in order[i][1]:
            return i
        else:
            i = ''

    return i

while True:
    north = []
    east = []
    south = []
    west = []

    deck = []

    partner = {
            'north':'',
            'east':'',
            'south':'',
            'west':''
        }

    order = {
            'north':[1j, north],
            'east':[1, east],
            'south':[-1j, south],
            'west':[-1, west]
        }

    table = {
            'north':['',0,0],
            'south':['',0,0],
            'east':['',0,0],
            'west':['',0,0]
        }

    cardmap = {
                '2':2,
                '3':3,
                '4':4,
                '5':5,
                '6':6,
                '7':7,
                '8':8,
                '9':9,
                '10':10,
                'J':11,
                'Q':12,
                'K':13,
                'A':14
        }        

    # build card deck
    for i in ['C','D','H','S']:
        for j in cardmap:
            deck.append(j+' '+i)

    # count HCP
    valid = 0

    while(valid<3):
        random.shuffle(deck)

        HCP = 0

        for i in range(4):
            for j in range(13):
                if cardmap[deck[(i*13)+(j)][:-2]] - 10 > 0:
                    HCP += cardmap[deck[(i*13)+(j)][:-2]] - 10

            # conditions leading to insufficient HCP
            if HCP>28 or HCP<4:
                break

            HCP = 0
            valid = i

    # Distribute cards to players
    for player in [north,south,east,west]:
        giveCards(player)

    ################
    ## Game start ##
    ################

    curPlayer = ''

    while curPlayer not in table:
        curPlayer = input('Who bids first? (North, East, South or West)\n')
        curPlayer = curPlayer.lower()

    print()

    trumpSuit = ''
    bid = ['name','bid']
    newBid = ''
    curBid = ''
    passes = 4

    turnTracker = order[curPlayer][0]

    validBids = []

    # list of valid bids
    for i in ['C','D','H','S','N']:
        for j in range(1,8):
            validBids.append(str(j)+i)

    # bidding
    while passes > 0:
        while True:
            print(curPlayer.upper()+' to bid.\n')
            print(handDisp(order[curPlayer][1]))
            newBid = input('What do you want to bid? (E.g. "1c" for 1 Club, "1n" for 1 No-Trump)\n')
            print()

            if (newBid.upper() in validBids) or ('P' in newBid.upper()):
                break
            else:
                print('Bid is invalid!\n')

        # when a player passes
        if 'P' in newBid.upper():
            passes -= 1
            turnTracker /= 1j

            for i in order:
                if order[i][0] == turnTracker:
                    curPlayer = i
                    
        # when a player bids lower than current bid
        elif newBid <= curBid:
            print('Please top-up your bid.\n')
            continue
        # normal bid
        else:
            curBid = newBid
            passes = 3
            turnTracker /= 1j
            
            for i in order:
                if order[i][0] == turnTracker:
                    curPlayer = i

    if curBid == '':
        print("Everyone passes. Reshuffling deck.\n")
        continue

    # store bid winner's name and winning bid
    bid[0] = curPlayer
    bid[1] = curBid

    # set bid winner as opener
    for i in order:
        if order[i][0] == turnTracker:
            curPlayer = i

    # asking for winner's partner
    print(curPlayer.upper()+" to choose partner.")
    while True:
        partnerCard = input("Who will be your partner? (e.g. 'A C', 'K D', etc.)\n")
        partnerCard = partnerCard.upper()
        
        if partnerCard in order[curPlayer][1]:
            print("That's your own card!\n")
            continue

        # assigning partnership to bid winner
        partner[curPlayer] = getPartner(partnerCard)

        if partner[curPlayer] == '':
            print("Invalid card!\n")
        else:
            partner[partner[curPlayer]] = curPlayer
            break
        
    print()

    # announce bid winner's partner
    print(curPlayer.upper()+"'s partner is '"+partnerCard+"'.\n")
    
    

    # assigning partnership to defender
    defender = ''
    
    for i in order:
        if partner[i] == '':
            if defender == '':
                defender = i
                continue
            else:
                partner[i] = defender
                partner[defender] = i

    playedCards = []
    winner = ''
    curSuit = ''
    counter = 1
    trumpBroke = False
    trumpSuit = bid[1][-1].upper()

    print('################')
    print('## GAME START ##')
    print('##  Trump:',trumpSuit,' ##')
    print('################\n')

    while winner == '':
        # show current player's hand and ask for input
        while not table[curPlayer][0] in order[curPlayer][1]:
            print(curPlayer.upper() + " to play\n")
            print('Current Suit :',curSuit,'\n')

            if playedCards != []:
                print('Cards played : ', end ='')
                for i in playedCards:
                    print(i,'>> ')

                print('[your turn]\n')
            
            print(handDisp(order[curPlayer][1]))
                
            table[curPlayer][0] = input('What to play? (Type the card exactly as displayed above)\n')
            table[curPlayer][0] = table[curPlayer][0].upper()

            if not table[curPlayer][0] in order[curPlayer][1]:
                print('Invalid play!\n')
                
        # take starter's suit as current suit
        if curSuit == '':
            curSuit = table[curPlayer][0][-1]
        
        # play trump
        if trumpSuit in table[curPlayer][0][-2:].upper():
            # opening trump
            if playedCards == [] and trumpBroke == False:
                print('Trump has not been broken!\n')
                table[curPlayer][0] = ''
                curSuit = ''
                continue
            
            # check for illegal trump play
            handString = ''
            for i in order[curPlayer][1]:
                handString += i

            if curSuit in handString:
                print('You are not allowed to play trump!\n')
                table[curPlayer][0] = ''
                continue

            # legit trump play
            trumpBroke = True           
            table[curPlayer][1] = cardmap[table[curPlayer][0][:-2]] + 100

        # follow
        elif table[curPlayer][0][-1] == curSuit:
            table[curPlayer][1] = cardmap[table[curPlayer][0][:-2]]
            
        # show out
        else:
            table[curPlayer][1] = -1

        # record played cards
        playedCards.append(table[curPlayer][0])
        
        print(curPlayer.upper()+' plays "'+table[curPlayer][0]+'"\n')
        
        # remove played card from hand
        order[curPlayer][1].remove(table[curPlayer][0])
            
        # end of round
        if counter == 4:
            # check for the winner of the round
            curWinner = ''
            winValue = 0

            for i in table:
                if table[i][1] > winValue:
                    winValue = table[i][1]
                    curWinner = i

            table[curWinner][2] += 1

            curPlayer = curWinner
            print(curWinner.upper()+' wins.\n')
            counter = 1
            turnTracker = order[curWinner][0]
            curSuit = ''
            playedCards = []

            # check for end of game
            if curWinner == bid[0]:
                # if declarer wins
                if table[curWinner][2] + table[partner[curWinner]][2] == int(bid[1][0]) + 6:
                    winner = curWinner
            else:
                # if defenders win
                if table[curWinner][2] + table[partner[curWinner]][2] == 14 - (int(bid[1][0]) + 6):
                    winner = curWinner

        else:
            counter += 1
            turnTracker /= 1j

            for i in order:
                if order[i][0] == turnTracker:
                    curPlayer = i
                    
    print('Winners are',winner.upper(),'and',partner[winner].upper())
