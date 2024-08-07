import random

class Karte:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol
    def __str__(self):
        return f"{self.color}, {self.symbol}"
  
colors = ["Kreuz", "Karo", "Herz", "Piek"]
symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Matrix = {}



def main():
    print("Hello, this is Poker Simulator Version Beta.1 ")
    all_cards = create_deck()
    while True:
        try:
            opponent_count = int(input("How many enemys do you wanna have? Min: 2, Max: 5. "))
            if 2 <= opponent_count <= 5:
                break
            else:
                pass
        except KeyboardInterrupt:
            exit() 
        except TypeError:
            pass
    used = game_start(opponent_count, all_cards)
    ingame_cards = used[0]
    middle_cards = used[1]
    players, community_cards = check_winner(middle_cards, ingame_cards)



def game_start(op_count, card_deck):
    middle_cards = {}
    card_return = deal_cards(op_count, card_deck)
    remain_cards = card_return[0]
    ingame_cards = card_return[1]
    print(f'{len(remain_cards)}')
    print(f'{len(ingame_cards)}')
    # Flop
    print(f'______________________ Flop _____________________', end='\n\n')
    flopp = flop(remain_cards, 3, middle_cards)
    flop_cards = flopp[1]
    for key in sorted(flop_cards.keys()):
        print(f'{key}: {flop_cards[key]}')
    # Turn
    print(f'_____________________ Turn ______________________', end='\n\n')
    turnn = turn(remain_cards, middle_cards)
    remain_cards = turnn[0]
    middle_cards = turnn[1]
    turn_card = middle_cards['turn']
    print(f'{turn_card}')
    # River 
    print(f'_____________________ River _____________________', end='\n\n')
    riverr = river(remain_cards, middle_cards)
    remain_cards = riverr[0]
    middle_cards = riverr[1]
    river_card = middle_cards['river']
    print(f'{river_card}', end='\n\n')
    return ingame_cards, middle_cards


def create_deck():
    i = 0
    for color in colors:
        n = 0
        for symbol in symbols:
            Matrix[(i, n)] = Karte(color, symbol)
            n += 1 
        i += 1
    # Print all cards
    '''for (i, n), karte in Matrix.items():
        print(f"({i}{n}): {karte}")'''
    return Matrix

def deal_cards(bot_count, card_deck):
    ingame_cards = {}
    remain_deck = card_deck
 
    for x in range(2):
        remain_deck, card = deal_card_user(remain_deck)
        ingame_cards[f'usercard{x}'] = card
        print(f'usercard{x}: {ingame_cards[f"usercard{x}"]}')

    for i in range(bot_count):
        for j in range(2):
            remain_deck, card = deal_card_bot(remain_deck)
            ingame_cards[f'bot{i}card{j}'] = card
            print(f'bot{i}card{j}: {card}')

    return remain_deck, ingame_cards

def deal_card_bot(d):
    try:
        i = str(random.randint(0, 3))
        n = str(random.randint(0, 12))
        bot_card = d[int(i),int(n)]
        del d[int(i),int(n)]
        return d, bot_card
    except KeyError:
        return deal_card_bot(d)

def deal_card_user(d):#
    try:
        i = str(random.randint(0, 3))
        n = str(random.randint(0, 12))
        user_card = d[int(i),int(n)]
        del d[int(i),int(n)]
        return d, user_card
    except KeyError:
        return deal_card_user(d)
    
def flop(d, x, middle_card):
    if x >= 1:
        try:
            i = str(random.randint(0, 3))
            n = str(random.randint(0, 12))
            new_card = d[int(i),int(n)]
            del d[int(i),int(n)]
            middle_card[f'flop_{x}'] = new_card
            return flop(d, x-1, middle_card)
        except KeyError:
            return flop(d, x, middle_card)
    else:
        return d, middle_card

def turn(d, middle_card):
    while True:
        try:
            i = str(random.randint(0, 3))
            n = str(random.randint(0, 12))
            new_card = d[int(i),int(n)]
            del d[int(i),int(n)]
            middle_card[f'turn'] = new_card
            return d, middle_card
        except KeyError:
            pass
    
def river(d, middle_card):
    while True:
        try:
            i = str(random.randint(0, 3))
            n = str(random.randint(0, 12))
            new_card = d[int(i),int(n)]
            del d[int(i),int(n)]
            middle_card[f'river'] = new_card
            return d, middle_card
        except KeyError:
            pass

def check_winner(middle_cards, ingame_cards):
    community_cards = {
        key: (card.color, card.symbol) for key, card in middle_cards.items()
    }
    players = {}
    for key, card in ingame_cards.items():
        if key.startswith('usercard'):
            player = 'user'
        else:
            player = key.split('card')[0]  # This will be 'bot0', 'bot1', etc.
        
        if player not in players:
            players[player] = {'hole_cards': [], 'hand': None, 'hand_rank': None}
        
        players[player]['hole_cards'].append((card.color, card.symbol))
        print("Community Cards:", list(community_cards.values()))
        for player, data in players.items():
                print(f"{player.capitalize()} Hole Cards:", data['hole_cards'])

        return players, community_cards






#def combine_cards()
main()