# Terminal Texas Hold'em (v4.0)

A lightweight, text-based Texas Hold'em poker engine built in Python. This game brings an authentic casino experience to your command line, featuring a full game loop, a robust wagering system, and a sophisticated hand evaluator.

##  Features

**Full Game Loop:** Experience every stage of a hand, including Pre-Flop, Flop, Turn, and River betting rounds.
**Advanced Hand Evaluation:** Automatically calculates winners based on full poker rankings, from *High Card* up to a *Royal Flush*.
**Custom Betting System:** A flexible wagering engine that allows players to input specific chip amounts for every bet.
**Validation & Safety:** Built-in exception handling ensures players cannot bet more than their current balance or go below the table minimum.
**Colourised Interface:** Integrated **Colorama** support for high-contrast, coloured terminal text, including red suits for *Hearts* and *Diamonds*.
**Paced Gameplay:** Includes artificial delays to mimic the natural rhythm of a real-life dealer.

## Getting Started

### Prerequisites
* Python 3.6 or higher.
* **Colorama** library (Required for v4.0+).

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/souryoghosh07/Terminal-Texas-Hold-em-](https://github.com/souryoghosh07/Terminal-Texas-Hold-em-)
    ```
2.  Install dependencies:
    ```bash
    pip install colorama
    ```
3.  Run the game:
    ```bash
    python poker_game.py
    ```

##  How to Play

1.  **The Deal:** You and the CPU start with 1,000 chips. You are dealt two private cards.
2.  **The Betting:** When prompted, enter a numeric value:
    * **Call/Raise:** Enter any amount equal to or greater than the table minimum.
    * **Fold:** Enter `0` to surrender the hand.
3.  **The Showdown:** After the River, the engine evaluates both hands and awards the pot to the winner based on official poker rules.

##  Version History

* **v1.0:** Basic game engine with evaluation up to Three of a Kind.
* **v2.0:** Implemented full rankings (up to Royal Flush) and standard Call/Raise/Fold logic.
* **v3.0:** Transitioned to a custom numeric betting system with strict input validation.
* **v4.0:** Added **Colorama** integration for coloured terminal UI.
