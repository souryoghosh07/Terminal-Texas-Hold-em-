import random
import time
from collections import Counter

class PokerGame:
    def __init__(self):
        self.ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                      '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.suits = ['♥', '♦', '♣', '♠']
        self.player_chips = 1000
        self.cpu_chips = 1000

    def format_card(self, card):
        return f"[{card[0]}{card[1]}]"

    def evaluate(self, hand):
        values = sorted([self.ranks[c[0]] for c in hand], reverse=True)
        counts = Counter(values)
        freq = sorted(counts.values(), reverse=True)
        if freq == [4, 1]: return (8, values) 
        if freq == [3, 2]: return (7, values)
        if freq == [3, 1, 1]: return (4, values)
        if freq == [2, 2, 1]: return (3, values)
        if freq == [2, 1, 1, 1]: return (2, values)
        return (1, values)

    def betting_round(self, round_name, community, player_hand, pot):
        print(f"\n" + "="*35)
        print(f" ROUND: {round_name.upper()}")
        print(f" POT  : {pot} | WALLET: {self.player_chips}")
        print(f" TABLE: {' '.join([self.format_card(c) for c in community]) if community else '[ Empty ]'}")
        print(f" HAND : {' '.join([self.format_card(c) for c in player_hand])}")
        print("="*35)
        
        while True:
            action = input("Action -> [C]all (10) or [F]old: ").lower()
            if action == 'f':
                return -1, pot
            if action == 'c':
                bet_amount = 10
                if self.player_chips < bet_amount:
                    print("Not enough chips! Going All-in.")
                    bet_amount = self.player_chips
                
                # UPDATE WALLETS HERE
                self.player_chips -= bet_amount
                self.cpu_chips -= bet_amount
                return bet_amount, pot + (bet_amount * 2)
            
            print("Invalid input. Type 'c' or 'f'.")

    def play_hand(self):
        deck = [(r, s) for s in self.suits for r in self.ranks]
        random.shuffle(deck)
        pot = 0
        community = []
        
        # 1. PRE-FLOP
        player_hand = [deck.pop(), deck.pop()]
        cpu_hand = [deck.pop(), deck.pop()]
        
        bet, pot = self.betting_round("Pre-Flop", community, player_hand, pot)
        if bet == -1: return "CPU takes the pot."

        # 2. THE FLOP
        print("\nDealing the Flop...")
        time.sleep(1)
        community.extend([deck.pop(), deck.pop(), deck.pop()])
        bet, pot = self.betting_round("The Flop", community, player_hand, pot)
        if bet == -1: return "CPU takes the pot."

        # 3. THE TURN
        print("\nDealing the Turn...")
        time.sleep(1)
        community.append(deck.pop())
        bet, pot = self.betting_round("The Turn", community, player_hand, pot)
        if bet == -1: return "CPU takes the pot."

        # 4. THE RIVER
        print("\nDealing the River...")
        time.sleep(1)
        community.append(deck.pop())
        bet, pot = self.betting_round("The River", community, player_hand, pot)
        if bet == -1: return "CPU takes the pot."

        # 5. SHOWDOWN
        print(f"\n--- SHOWDOWN ---")
        print(f"Your Hand: {' '.join([self.format_card(c) for c in player_hand])}")
        print(f"CPU Hand : {' '.join([self.format_card(c) for c in cpu_hand])}")
        
        p_val = self.evaluate(player_hand + community)
        c_val = self.evaluate(cpu_hand + community)

        if p_val > c_val:
            print(f"*** YOU WIN THE POT OF {pot}! ***")
            self.player_chips += pot
        elif c_val > p_val:
            print(f"*** CPU WINS THE POT OF {pot}! ***")
            self.cpu_chips += pot
        else:
            print("*** Draw! Pot split. ***")
            self.player_chips += pot // 2
            self.cpu_chips += pot // 2
        
        return "Hand Complete."

# Start Game
game = PokerGame()
print("Welcome to Terminal Texas Hold'em!")
while game.player_chips > 0 and game.cpu_chips > 0:
    msg = game.play_hand()
    print(msg)
    if game.player_chips <= 0:
        print("Game Over! You're out of chips.")
        break
    if input("\nDeal again? (y/n): ").lower() != 'y':
        break

print(f"Final Score - You: {game.player_chips} | CPU: {game.cpu_chips}")