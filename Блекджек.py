import random, sys
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824) 
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''
   Правила:
      Спробуйте наблизитися до 21, не перебравши.
      Королi, дами та валети коштують 10 очок.
      Тузи оцiнюються в 1 або 11 очок.
      Картки вiд 2 до 10 мають свою номiнальну вартiсть.
      (H) щоб взяти ще одну картку.
      (S) припинити брати карти.
      Пiд час першої гри ви можете натиснути"D"(подвоїти), щоб збiльшити свою
      ставку, але потрiбно взяти карту рiвно ще один раз, перш нiж розкритися.
      У разi нiчиєї ставка повертається гравцевi.
      Дилер припиняє брати карти на 17.

   ''')

    money = 5000
    while True:  
        if money <= 0:
            print("Ти банкрот!")
            print("Добре що не грав(-ла) зi справжнiми грошми.")
            print('Дякую за гру!')
            input()
            sys.exit()
        print('Грошi:', money)
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        print('Ставка:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)
            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Ставка пiдвищується до {}.'.format(bet))
                print('Ставка:', bet)
            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('Ви взяли карту {} мастi {}.'.format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ('S', 'D'):
                break
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print('Дилер ходить бере карту...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break  
                input('Натиснiть Enter щоб продовжити...')
                print('\n\n')
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue > 21:
            print('Дилер програв! Ти отримуєш ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Ти програв!')
            money -= bet
        elif playerValue > dealerValue:
            print('Ти виграв ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('Нiчия. Ставка повертається тобi.')
        input('Натиснiть Enter щоб продовжити...')
        print('\n\n')


def getBet(maxBet):
    while True:
        print('Скiльки ви хочете поставити? (1-{}, або ВИХIД)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'ВИХIД':
            print('Дякую за гру!')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) 
        for rank in ('В', 'Д', 'К', 'Т'):
            deck.append((rank, suit)) 
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('Дилер:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Дилер: ???')
        displayCards([BACKSIDE] + dealerHand[1:])
    print('Гравець:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]  
        if rank == 'Т':
            numberOfAces += 1
        elif rank in ('К', 'Д', 'В'):  
            value += 10
        else:
            value += int(rank)  
    value += numberOfAces  
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


def displayCards(cards):
    rows = ['', '', '', '', '']  
    for i, card in enumerate(cards):
        rows[0] += ' ___  '  
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card  
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ['(H)Взяти карту', '(S)Пас']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)Подвiйна ставка')
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  
        if move == 'D' and '(D)Подвiйна ставка' in moves:
            return move  


if __name__ == '__main__':
    main()
