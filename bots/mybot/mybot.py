"""
MyBot -- A simple strategy:
1. Try to play a marriage
2a. If the opponent has the lead you play a card that beats it
2b. If you don't have a card that beats your opponents card you play your lowest card.
3. If you lead you play your highest card.
"""

# Import the API objects
from api import State
import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        # All legal moves
        moves = state.moves()

        for move in moves:
            if move[1]:  # move[1] exists if there is a marriage possible
                return move

        opp_card = state.get_opponents_played_card()
        if opp_card:
            for move in moves: # Choose the next best card that beats our opponent's played card
                if move[0] and opp_card % 5 < move[0] % 5:
                    return move

            chosen_move = moves[0]
            for move in moves: # Choose the worst card that loses to our opponent's played card
                if move[0] and move[0] % 5 >= chosen_move[0] % 5:
                    chosen_move = move
        else:
            chosen_move = moves[0]
            for move in moves:
                if move[0] and chosen_move[0] % 5 < move[0] % 5:
                    chosen_move = move

        return chosen_move