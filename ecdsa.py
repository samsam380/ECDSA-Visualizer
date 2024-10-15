# Define a function for elliptic curve point addition
# This is simplified for visualization purposes and does not handle edge cases like when points are the same or P == Q

def point_addition(P, Q):
    # P and Q are tuples (x, y)
    if P == Q:
        # Special case for point doubling (simplified here for visualization)
        slope = (3 * P[0]**2) / (2 * P[1])
    else:
        slope = (Q[1] - P[1]) / (Q[0] - P[0])
    
    x_r = slope**2 - P[0] - Q[0]
    y_r = slope * (P[0] - x_r) - P[1]
    
    return (x_r, y_r)

# Define initial points on the curve
G = (0.5, elliptic_curve(0.5))  # The generator point (G) approximated for real values

# Perform point addition G + G (point doubling)
R = point_addition(G, G)

# Plot the elliptic curve again and show point addition results
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label=r'$y^2 = x^3 + 7$', color='blue')
plt.plot(x_vals, -y_vals, color='blue')  # Plot the negative root as well

# Plot the generator point G
plt.scatter(G[0], G[1], color='red', label='Generator Point (G)', zorder=5)

# Plot the result of point addition R = G + G
plt.scatter(R[0], R[1], color='green', label='Result of G + G', zorder=5)

# Add labels and title
plt.title("Elliptic Curve with Point Addition", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

