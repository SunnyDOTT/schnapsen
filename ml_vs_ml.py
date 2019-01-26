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
from bots.mlfeat import mlfeat
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

win_rate_1 = []
win_rate_2 = []

match = 0
for _ in range(10):
    curr_win_rate_1 = []
    curr_win_rate_2 = []
    for bot in BOTS:
        player1 = ml.Bot(model_file=bot)
        player2 = mlfeat.Bot(model_file=bot.replace('/ml/', '/mlfeat/'))

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

        win_rate_1.append(bot1_wins/GAMES*100)
        win_rate_2.append(bot2_wins/GAMES*100)
        curr_win_rate_1.append(bot1_wins / GAMES * 100)
        curr_win_rate_2.append(bot2_wins / GAMES * 100)

        print("Match %d: ml/%s won: %d times, mlfeat/%s won: %d times" % (match, bot[bot.find('model_'):], bot1_wins,
                                                                            bot[bot.find('model_'):], bot2_wins))

    print("Session winrates: Bot ml has a win rate of %.2f%%, Bot mlfeat has a win rate of %.2f%%" % (
        sum(curr_win_rate_1) / len(curr_win_rate_1), sum(curr_win_rate_2) / len(curr_win_rate_1)))
    print("----------------------------------------------------------------------------------------------------------")

print("Final winrates: Bot ml has a win rate of %.2f%%, Bot mlfeat has a win rate of %.2f%%\n" % (sum(win_rate_1)/len(win_rate_1),
                                                                                sum(win_rate_2)/len(win_rate_1)))
