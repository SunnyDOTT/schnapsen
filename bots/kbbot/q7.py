import sys
from kb import KB, Boolean, Integer, Constant

# Init all cards & player cards :
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

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# I add all the cards J to T just for the lulz
for i in range(5, 25, 5):
    for j, k in zip(range(1, 6), range(0, 100, 20)):
        kb.add_clause(Deck[i - j + k])

# DEFINITION OF THE STRATEGY
# Play cheap cards first --> Cheap cards are: Jacks, Queens and Kings.
# We have: J4, J9. J14, J19 - Q3, Q8, Q13, Q18 - K2, K7, K12, K17
# The first nested loop defines the cheap cards.
for i in range(5, 25, 5):
    for j, k in zip(range(1, 4), range(0, 60, 20)):
        kb.add_clause(Cs[i - j], ~Deck[i - j + k])

# The next nested loop defines PC <-----> C
for i in range(5, 25, 5):
    for j in range(1, 4):
        kb.add_clause(Cs[i - j], ~PCs[i - j])
        kb.add_clause(~Cs[i - j], PCs[i - j])

# Toggle this to get a valid/invalid kb:
kb.add_clause(~PCs[4])
print(~PCs[4])
# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())