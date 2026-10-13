import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Set up the figure
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 6))

# ------------------------------------------------------------
# 2. Draw the prism (an isosceles triangle pointing up)
# ------------------------------------------------------------
A = (-1.0, -1.0)          # bottom-left
B = ( 1.0, -1.0)          # bottom-right
C = ( 0.0,  1.0)          # top
prism = plt.Polygon(
    [A, B, C],
    closed=True,
    facecolor='lightblue',
    edgecolor='black',
    linewidth=2,
    alpha=0.30
)
ax.add_patch(prism)

# ------------------------------------------------------------
# 3. Incoming white light ray (from left to the entry point)
# ------------------------------------------------------------
entry = (-0.5, 0.0)       # point where the ray hits the left face
start = (-3.5, 0.0)       # starting point of the white ray

# Draw a thick white line with a thin dashed black outline for visibility
ax.plot([start[0], entry[0]], [start[1], entry[1]],
        color='white', linewidth=6, solid_capstyle='round', zorder=3)
ax.plot([start[0], entry[0]], [start[1], entry[1]],
        color='black', linewidth=1.2, linestyle='--', alpha=0.6, zorder=4)

# ------------------------------------------------------------
# 4. Define the seven colors and their English labels
# ------------------------------------------------------------
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
labels = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# ------------------------------------------------------------
# 5. Calculate exit points on the right face (B to C)
#    Right face equation: x = 0.5 - y/2
# ------------------------------------------------------------
y_exit = np.linspace(-0.6, 0.6, 7)          # evenly spaced along the face
x_exit = 0.5 - y_exit / 2.0

# ------------------------------------------------------------
# 6. Define the end points of the outgoing rays (for the fan)
#    They are evenly spaced vertically to keep the labels apart.
# ------------------------------------------------------------
x_end = 4.5
y_end = np.linspace(-2.2, 2.2, 7)

# ------------------------------------------------------------
# 7. Draw internal rays (inside the prism) and outgoing rays
# ------------------------------------------------------------
for i in range(7):
    # Internal ray: from entry point to the exit point on the right face
    ax.plot([entry[0], x_exit[i]], [entry[1], y_exit[i]],
            color=colors[i], linewidth=2.2, alpha=0.9, zorder=2)
    
    # Outgoing ray: from exit point to the far-right end point
    ax.plot([x_exit[i], x_end], [y_exit[i], y_end[i]],
            color=colors[i], linewidth=2.2, zorder=2)
    
    # Place the label at the end of each outgoing ray
    # Add a small horizontal offset so text doesn't sit on the line
    ax.text(x_end + 0.15, y_end[i], labels[i],
            color=colors[i], fontsize=14, fontweight='bold',
            va='center', ha='left', zorder=5)

# ------------------------------------------------------------
# 8. Add a small marker at the entry point (optional)
# ------------------------------------------------------------
ax.scatter(entry[0], entry[1], color='white', s=40, zorder=6, edgecolor='black')

# ------------------------------------------------------------
# 9. Set limits and remove axes
# ------------------------------------------------------------
ax.set_xlim(-3.8, 6.2)
ax.set_ylim(-2.8, 2.8)
ax.axis('off')

# ------------------------------------------------------------
# 10. Title
# ------------------------------------------------------------
ax.set_title('Light Dispersion Through a Prism', fontsize=18, pad=15)

plt.tight_layout()
plt.show()