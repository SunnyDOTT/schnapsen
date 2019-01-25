"""

This script shows an example of how to run a simple computational experiment. The research
question is as follows:

    Which of the ML bots perform better?

The models are:
    1. model_rand.pkl
    2. model_ml.pkl
    3. model_rdeep.pkl

"""
import matplotlib as mpl
mpl.use('Agg')
from bots.ml import ml
from api import State, engine, util
import os
import random

# For experiments, it's good to have repeatability, so we set the seed of the random number generator to a known value.
# That way, if something interesting happens, we can always rerun the exact same experiment
seed = random.randint(1, 1000)
print('Using seed {}.'.format(seed))
random.seed(seed)

GAMES = 1000
BOTS = ['/bots/ml/model_rand.pkl', '/bots/ml/model_rdeep.pkl', '/bots/ml/model_ml.pkl']
BOTS = [os.path.dirname(os.path.realpath(__file__)) + s for s in BOTS]

win_rates = {
            BOTS[0]: [],
            BOTS[1]: [],
            BOTS[2]: []
}

match = 0

for bot1 in BOTS:
    for bot2 in BOTS:
        player1 = ml.Bot(model_file=bot1)
        player2 = ml.Bot(model_file=bot2)

        bot1_wins = 0
        bot2_wins = 0

        match += 1

        for i in range(GAMES):
                    state = State.generate()

                    # play the game
                    while not state.finished():
                        player = player1 if state.whose_turn() == 1 else player2
                        state = state.next(player.get_move(state))

                    if state.finished():
                        winner, points = state.winner()
                        if winner == 1:
                            bot1_wins += 1
                        else:
                            bot2_wins += 1

        win_rates[bot1].append(bot1_wins/GAMES*100)
        win_rates[bot2].append(bot2_wins/GAMES*100)

        print("Match %d: %s won: %d times, %s won: %d times\n" % (match, bot1[bot1.find('model_'):], bot1_wins,
                                                                  bot2[bot2.find('model_'):], bot2_wins))
for bot, win_rate in win_rates.items():
    print("Bot %s has a win rate of %.2f%%" % (bot[bot1.find('model_'):], sum(win_rate)/(len(BOTS)*2)))
