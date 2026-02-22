def evaluate_hands():

    return
def Remaining_cards(deck, total_cards):
    return [c for c in deck if c not in total_cards]

def bestcard(total_cards):
    if len(total_cards) >5 :

        return total_cards

    else:
        return total_cards






def get_action(my_cards,community_cards,player.current_bet,player.bet_amount, player.chips,game.pot,game.current_bet):
    #C = Clubs, H = hearts, D = diamonds, S = spades,
    deck = [
        "C_A","C_K","C_Q","C_J","C_10","C_9","C_8","C_7","C_6","C_5","C_4","C_3","C_2","C_1",
        "H_A","H_K","H_Q","H_J","H_10","H_9","H_8","H_7","H_6","H_5","H_4","H_3","H_2","H_1",
        "D_A","D_K","D_Q","D_J","D_10","D_9","D_8","D_7","D_6","D_5","D_4","D_3","D_2","D_1",
        "S_A","S_K","S_Q","S_J","S_10","S_9","S_8","S_7","S_6","S_5","S_4","S_3","S_2","S_1"
    ]

    total_cards = []
    total_cards.append(my_cards)
    total_cards.append(community_cards)
    remaining_cards = Remaining_cards(deck,total_cards)
    best_card = bestcard(total_cards)

    my_sequence = evaluate_hands(total_cards)

    cards_favouring_me = calc_cards_favouring_me(best_card)
    if game.current_bet -player.bet_amount > 0:
        pot_odds = game.pot/(game.current_bet -player.bet_amount )
    else:
        pot_odds = game.pot/player.bet_amount 

    odds_against_calc  = (52 - len(total_cards) - cards_favouring_me)/cards_favouring_me
    
    if pot_odds > odds_against_calc:
        action = "call" or "bet" or "raise"

    else:
        action = "check" or "fold"
    return action





def calc_cards_favouring_me(deck,total_cards):
    
    cards_favouring_me = 
    
    
    return cards_favouring_me






