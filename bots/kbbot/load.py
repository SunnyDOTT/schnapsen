from .kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
cards = ['j', 'q', 'k', 't', 'a']

Deck = []   # The entire deck -- 0, 19 = Jacks, 20, 39 = Queens, etc.
Cs = []
PCs = []    # PlayerCards -- ^

for card in cards:
    for i in range(0, 20):
        Deck.append(Boolean('%s%d' % (card, i)))
        if len(Cs) < 20:
            Cs.append(Boolean('c%d' % i))
            PCs.append(Boolean('pc%d' % i))


def trump_wedding_info(kb):
    pass


def trump_wedding_strat(kb):
    pass


# ---- Cheap Card Strat ----
def cheap_card_info(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    for i in range(5, 25, 5):
        for j, k in zip(range(1, 6), range(0, 100, 20)):
            kb.add_clause(Deck[i - j + k])


def cheap_card_strat(kb):
    # DEFINITION OF THE STRATEGY
    # Add clauses (This list is sufficient for this strategy)
    for i in range(5, 25, 5):
        for j, k in zip(range(1, 4), range(0, 60, 20)):
            kb.add_clause(Cs[i - j], ~Deck[i - j + k])

    # The next nested loop defines PC <-----> C
    for i in range(5, 25, 5):
        for j in range(1, 4):
            kb.add_clause(Cs[i - j], ~PCs[i - j])
            kb.add_clause(~Cs[i - j], PCs[i - j])