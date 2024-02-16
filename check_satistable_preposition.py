from sympy import symbols, Or, Implies, satisfiable, Not

# Definizione delle variabili proposizionali
A, B = symbols('A B')

# Definizione dell'espressione A OR B → B OR A
expression = Implies(Or(A, B), Or(B, A))
# Verifica della soddisfacibilità
result = satisfiable(expression)

print(result)
