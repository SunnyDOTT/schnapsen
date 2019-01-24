import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our symbols
A = Boolean('A')
B = Boolean('B')
C = Boolean('C')
D = Boolean('D')

# Create a new knowledge base
kb = KB()

# Add clauses
kb.add_clause(A, B)     # A v B
kb.add_clause(~B, A)    # -B v A
kb.add_clause(~A, C)    # a. -A v C) /\
kb.add_clause(~A, D)    # b. (-A v D)

# Print all models of the knowledge base
for model in kb.models():
    print(model)

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())
