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
        vals = sorted([self.ranks[c[0]] for c in hand], reverse=True)
        suits = [c[1] for c in hand]
        counts = Counter(vals)
        freq = sorted(counts.values(), reverse=True)
        
        suit_counts = Counter(suits)
        is_flush = any(count >= 5 for count in suit_counts.values())
        
        unique_vals = sorted(list(set(vals)), reverse=True)
        is_straight = False
        straight_high = 0
        if len(unique_vals) >= 5:
            for i in range(len(unique_vals) - 4):
                if unique_vals[i] - unique_vals[i+4] == 4:
                    is_straight = True
                    straight_high = unique_vals[i]
                    break
            if {14, 2, 3, 4, 5}.issubset(set(unique_vals)):
                is_straight = True
                straight_high = 5
        
        if is_straight and is_flush:
            if straight_high == 14: return (10, "ROYAL FLUSH")
            return (9, "STRAIGHT FLUSH")
        if freq == [4, 1, 1, 1] or freq == [4, 1]: return (8, "FOUR OF A KIND")
        if freq == [3, 2] or freq == [3, 2, 2]: return (7, "FULL HOUSE")
        if is_flush: return (6, "FLUSH")
        if is_straight: return (5, "STRAIGHT")
        if freq[0] == 3: return (4, "THREE OF A KIND")
        if freq[:2] == [2, 2]: return (3, "TWO PAIR")
        if freq[0] == 2: return (2, "ONE PAIR")
        return (1, "HIGH CARD")

    def betting_round(self, round_name, community, player_hand, pot):
        print(f"\n" + "="*35)
        print(f" ROUND: {round_name.upper()}")
        print(f" POT  : {pot} | WALLET: {self.player_chips}")
        print(f" TABLE: {' '.join([self.format_card(c) for c in community]) if community else '[ Empty ]'}")
        print(f" HAND : {' '.join([self.format_card(c) for c in player_hand])}")
        print("="*35)
        
        while True:
            action = input("Action -> [C]all (10), [R]aise (50), or [F]old: ").lower()
            if action == 'f':
                return -1, pot
            if action == 'c' or action == 'r':
                bet_amount = 10 if action == 'c' else 50
                if self.player_chips < bet_amount:
                    bet_amount = self.player_chips
                self.player_chips -= bet_amount
                self.cpu_chips -= bet_amount
                return bet_amount, pot + (bet_amount * 2)
            print("Invalid input. Type 'c', 'r', or 'f'.")

    def play_hand(self):
        deck = [(r, s) for s in self.suits for r in self.ranks]
        random.shuffle(deck)
        pot = 0
        community = []
        
        player_hand = [deck.pop(), deck.pop()]
        cpu_hand = [deck.pop(), deck.pop()]
        bet, pot = self.betting_round("Pre-Flop", community, player_hand, pot)
        if bet == -1: return "CPU takes the pot."

        for stage, count in [("The Flop", 3), ("The Turn", 1), ("The River", 1)]:
            print(f"\nDealing {stage}...")
            time.sleep(0.5)
            for _ in range(count): community.append(deck.pop())
            bet, pot = self.betting_round(stage, community, player_hand, pot)
            if bet == -1: return "CPU takes the pot."

        print(f"\n--- SHOWDOWN ---")
        p_val, p_desc = self.evaluate(player_hand + community)
        c_val, c_desc = self.evaluate(cpu_hand + community)

        print(f"Your Hand: {' '.join([self.format_card(c) for c in player_hand])} -> {p_desc}")
        print(f"CPU Hand : {' '.join([self.format_card(c) for c in cpu_hand])} -> {c_desc}")
        
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

game = PokerGame()
print("Welcome to Terminal Texas Hold'em! - v2.0")

while game.player_chips > 0 and game.cpu_chips > 0:
    msg = game.play_hand()
    print(msg)
    if game.player_chips <= 0:
        print("Game Over! You're out of chips.")
        break
    if input("\nDeal again? (y/n): ").lower() != 'y':
        break

print(f"Final Score - You: {game.player_chips} | CPU: {game.cpu_chips}")