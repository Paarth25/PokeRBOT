from game_structure import Player, Pokergame
from bet_or_not import get_action
from what_to_bet import get_amount

players = []
num_players = int(input("How many Players? "))

for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    chips = int(input("Enter starting chips: "))
    players.append(Player(name,chips,is_human=True))

players.append(Player("me",1000,is_human=False))

game = Pokergame(players)

print("\nPlayers at table:")
for i, player in enumerate(players):
    print(i, "-", player.name)


dealer_name = input("\nWhat is the name of dealer? ")

for i, player in enumerate(players):
    if player.name == dealer_name:
        game.dealer_index = i
        break


small_blind = 10
big_blind = 20

my_cards = input("Enter my cards (space separated): ").split()
community_cards = []

sb_index,bb_index = game.post_blinds(small_blind,big_blind)

rounds = ["Preflop","flop","turn","river"]

for round_name in rounds:

    print(f"\n--- Current Round: {round_name} ---")

    if round_name == "Preflop":
        start_index = (bb_index + 1) % len(players)
    else:
        start_index = (sb_index) % len(players)

    game.current_player_index = start_index

    print("Starting player:", players[start_index].name)
    print("Start betting/n")
    betting_round_active = True

    while betting_round_active:
        for i in range(len(players)):

            player_index = (start_index + i) % len(players)
            player = players[player_index]

            if player.status != "active":
                continue

            print(f"\n{player.name}'s turn")

            if player.is_human == False:

                action = get_action(
                    my_cards,
                    community_cards,
                    player.current_bet,
                    player.bet_amount, 
                    player.chips,
                    game.pot,
                    game.current_bet
                )

                if action in ["bet", "raise"]:
                    amount = get_amount(game, player)
                else:
                    amount = 0
                
            else:
                if game.current_bet == 0:
                    print("Available actions: check, bet, fold")
                else:
                    print("Available actions: call, raise, fold")

                action = input("Enter action: ")

                if action in ["bet", "raise"]:
                    amount = int(input("Enter amount: "))
                else:
                    amount = 0

            game.player_action(player, action, amount)

        all_matched = True

        for p in players:
            if p.status == "active" and p.current_bet != game.current_bet:
                all_matched = False
                break

        if all_matched:
            betting_round_active = False
    for p in players:
        p.current_bet = 0

    game.current_bet = 0

    if round_name == "Flop":
        flop = input("Enter flop cards (3 cards space separated): ").split()
        community_cards.extend(flop)

    elif round_name == "Turn":
        turn = input("Enter turn card: ")
        community_cards.append(turn)

    elif round_name == "River":
        river = input("Enter river card: ")
        community_cards.append(river)
            
