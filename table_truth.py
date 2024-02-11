import pandas as pd
import itertools

# Define the expressions as lambda functions
expr1 = lambda A, B:  A and  B  # (A ∧ B)
expr2 = lambda C: C  # C
expr3 = lambda A, C:  A and C  # (A ∧ C)

# Generate truth values
values = [True, False]

# Create a truth table
truth_table = pd.DataFrame(list(itertools.product(values, repeat=3)), columns=['A', 'B', 'C'])

# Apply the expressions to the truth table
truth_table['(A ∧ B)'] = truth_table.apply(lambda row: expr1(row['A'], row['B']), axis=1)
truth_table['(A ∧ C)'] = truth_table.apply(lambda row: expr3(row['A'], row['C']), axis=1)
truth_table['(A ∧ B) → [C → (A ∧ C)]'] = truth_table.apply(lambda row: not row['(A ∧ B)'] or (not row['C'] or row['(A ∧ C)']), axis=1)

# Display the truth table
truth_table[['A', 'B', 'C', '(A ∧ B)', '(A ∧ C)', '(A ∧ B) → [C → (A ∧ C)]']]
print(truth_table)
