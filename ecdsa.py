# first install widgets with this command: pip install ipywidgets

import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Function for the elliptic curve y^2 = x^3 + 7 (over real numbers)
def elliptic_curve(x):
    return np.sqrt(x**3 + 7)

# Define the range of x-values (for real numbers)
x_vals = np.linspace(-3, 3, 1000)

# Calculate the corresponding y-values for the elliptic curve (only the positive root)
y_vals = elliptic_curve(x_vals)

# Define a function for elliptic curve point addition
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

# Define a function to plot the curve and points dynamically based on user input
def update_plot(Px, Py, Qx, Qy):
    # Convert inputs into points P and Q
    P = (Px, Py)
    Q = (Qx, Qy)
    
    # Perform point addition
    R = point_addition(P, Q)

    # Plot the elliptic curve
    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, label=r'$y^2 = x^3 + 7$', color='blue')
    plt.plot(x_vals, -y_vals, color='blue')  # Plot the negative root as well

    # Plot the points P, Q, and the result R
    plt.scatter(P[0], P[1], color='red', label=f'Point P ({P[0]:.2f}, {P[1]:.2f})', zorder=5)
    plt.scatter(Q[0], Q[1], color='orange', label=f'Point Q ({Q[0]:.2f}, {Q[1]:.2f})', zorder=5)
    plt.scatter(R[0], R[1], color='green', label=f'Point R = P + Q ({R[0]:.2f}, {R[1]:.2f})', zorder=5)

    # Add labels and title
    plt.title("Elliptic Curve with User-Defined Point Addition", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

# Widgets for inputting points
Px_slider = widgets.FloatSlider(min=-2, max=2, step=0.01, value=0.5, description='Px')
Py_slider = widgets.FloatSlider(min=-2, max=2, step=0.01, value=elliptic_curve(0.5), description='Py')
Qx_slider = widgets.FloatSlider(min=-2, max=2, step=0.01, value=1.0, description='Qx')
Qy_slider = widgets.FloatSlider(min=-2, max=2, step=0.01, value=elliptic_curve(1.0), description='Qy')

# Update the plot when sliders are changed
widgets.interactive(update_plot, Px=Px_slider, Py=Py_slider, Qx=Qx_slider, Qy=Qy_slider)

# Display the sliders and plot
display(Px_slider, Py_slider, Qx_slider, Qy_slider)
