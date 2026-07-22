# Project to practice Python OOP further. Now introducing Dunder methods and a rule-validation engine:

# Task - Build the game "Eleusis" for a single player
# Rules of the game:
# The dealer (the computer) picks a random hidden rule at the start of the game from a pool of 6 rules
# The dealer will shuffle a standard 52 card deck, place one down to start the sequence, and I as the player will get the rest of the cards
# At the start of my turn, I can look at my hand and the existing sequence of cards
# I can then select a card to play, and the dealer will say either "legal" or "illegal" depending on whether that card follows the dealer's hidden rule
# If the card is legal, it forms part of the card sequence. If it is illegal, the card is rejected and goes back into my hand
# To win, I need to either play my whole hand legally, or guess the hidden rule correctly

# Features to work on in this project:
# Using dunder methods to create the functionality of the game and allow for comparison of two cards, etc.
# I want the player to be able to use free/human text to guess the hidden rule. So I'll be developing a keyword-matching functionality, as well as a feature to catch ambiguity
# in case the player's guess fits the keyword search for more than one rule

# This will be my first attempt at a "card game" program with card interactions. Excited to try my hand at this
# Similar to zookeeper.py, I will not be including any input validation/edge-case handling/type errors, etc. unless it's directly
# tied to the functioning of the game. This is a focused exercise on practicing new concepts, not old ones that I already know

# This will be my first project where I am using Pytest and a linter (Ruff) to set up good habits and good practice going forward

# I suspect I will need the following classes, to keep functionalities seperated cleanly:
# Card - Handles what the cards are and can compare cards to each other
# Deck - Shuffles the deck, plays the first card, and gives the player their hand
# Rules - Contains the hidden rules, has the randomly selected rule for the game, and can validate a player's guess
# Sequence - Holds the growing list of legally played cards
# Game/Play - Contains the actual gameplay loop that the player plays

import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.values = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        self.card_deck = [
            Card(suit, value) for suit in self.suits for value in self.values
        ]

    def shuffle_deck(self):
        random.shuffle(self.card_deck)

    def deal_cards(self):
        starting_card = self.card_deck.pop(0)
        player_hand = self.card_deck.copy()

        # Emptying the card_deck as a guard rail against accidental future reference to the deck, which shouldnt happen past this point

        self.card_deck = []

        return starting_card, player_hand

# Next up is testing a random rule against a card played. How are rules going to be represented? String? Function? Other?


class Rules:
    pass


class Sequence:

    def __init__(self, first_card):
        self.card_sequence = [first_card]
        self.card_history = [(first_card, "Starting Card")]

    def add_card(self, player_card):
        self.card_sequence.append(player_card)

    def show_sequence(self):
        return self.card_sequence

    def add_history(self, player_card, legal_state):
        self.card_history.append((player_card, legal_state))

    def show_history(self):
        return self.card_history

    def __len__(self):
        return len(self.card_sequence)


class Game:

    def run(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
