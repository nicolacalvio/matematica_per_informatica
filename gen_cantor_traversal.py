import matplotlib.pyplot as plt
import numpy as np

# Set the limit for the number of pairs (x, y) to be plotted
limit = 10

# Create a grid of points
x = np.arange(limit)
y = np.arange(limit)
X, Y = np.meshgrid(x, y)

# Flatten the arrays for plotting
X_flat = X.flatten()
Y_flat = Y.flatten()

# Generate the order for the Cantor pairing
order = sorted(range(len(X_flat)), key=lambda i: X_flat[i] + Y_flat[i])

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(X_flat[order], Y_flat[order], marker='o', linestyle='-')
plt.scatter(X_flat, Y_flat)

# Annotate some points for clarity
for i in range(min(len(X_flat), 10)):  # Annotate only the first few points
    plt.annotate(f'{X_flat[order][i]},{Y_flat[order][i]}', (X_flat[order][i], Y_flat[order][i]),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Cantor Diagonal Argument')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.xlim(-1, limit)
plt.ylim(-1, limit)
plt.show()
