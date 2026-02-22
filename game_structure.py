class Player:
    def __init__(self,name,chips,is_human):
        self.name = name
        self.chips = chips
        self.bet_amount = 0
        self.current_bet = 0
        self.status = "active"
        self.is_human = is_human

    def bet(self,amount):
        self.chips -= amount
        self.bet_amount += amount
        self.current_bet += amount
        return amount
    
    def fold(self):
        self.status = "folded"

class Pokergame:
    def __init__(self,players):
        self.players = players
        self.pot = 0
        self.current_bet = 0
        self.current_player_index = 0
        self.dealer_index = 0    

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        if self.players[self.current_player_index].status == "active":
            return


    def post_blinds(self,small_blind,big_blind):
        sb_index = (self.dealer_index+1) % len(self.players)
        bb_index = (self.dealer_index+2) % len(self.players)

        sb_player = self.players[sb_index]
        bb_player = self.players[bb_index]

        print(f"{sb_player.name} posts small blind: {small_blind}")
        print(f"{bb_player.name} posts big blind: {big_blind}")

        self.pot += sb_player.bet(small_blind)
        self.pot += bb_player.bet(big_blind)

        self.current_bet = big_blind  
        return (sb_index, bb_index)
    

    def player_action(self,action,amount =0):
        player = self.players[self.current_player_index]

        if action == "call":
            to_call = self.current_bet - player.current_bet
            if to_call > 0:
                self.pot += player.bet(to_call)

        elif action == "raise":
            to_pay =  amount - self.current_bet
            self.pot += player.bet(to_pay)
            self.current_bet = amount

        elif action == "fold":
            player.fold()

        elif action == "check":
            if self.current_bet == 0:
                print(player.name, "checks")
            else:
                print("Cannot check. Must call or raise.")

        elif action == "bet":
            if self.current_bet == 0:
                self.current_bet = amount
                self.pot += player.bet(amount) 

