import numpy as np
import matplotlib.pyplot as plt

# Gauge configuration
min_angle = -45
max_angle = 225
min_label = 0
max_label = 600
num_minor_steps = 60
tick_factor = 4
charcoal = '#202020'
facecolor=charcoal

# Geometry
r_outer = 1.0
r_major = 0.88
r_minor = 0.94
r_labels = 0.80

# Set limit values
minor_step = (int)(max_label/num_minor_steps)
major_step = minor_step*tick_factor

# Create polar plot
fig, ax = plt.subplots(
    figsize=(7, 7),
    subplot_kw={'projection': 'polar'},
    facecolor=facecolor
)

ax.set_facecolor(facecolor)

# Gauge orientation
ax.set_theta_zero_location("W")
ax.set_theta_direction(-1)

# Remove default polar decorations
ax.set_ylim(0, 1.25)
ax.set_axis_off()

# Values displayed on the gauge
labels = np.arange(min_label, max_label + 1, minor_step)

# Actual angular positions
angles = np.linspace(min_angle, max_angle, len(labels))

for angle, label in zip(angles, labels):

    theta = np.deg2rad(angle)

    major = label % major_step == 0

    r_inner = r_major if major else r_minor
    width = 2.0 if major else 0.8

    # Draw tick
    ax.plot(
        [theta, theta],
        [r_inner, r_outer],
        color='white',
        linewidth=width,
        solid_capstyle='butt'
    )

    # Numerical labels
    if major:
        ax.text(
            theta,
            r_labels,
            f'{label:.0f}',
            ha='center',
            va='center',
            fontsize=11,
            color='white'
        )

# Outer circumference
theta_circle = np.linspace(0, 2*np.pi, 500)

ax.plot(
    theta_circle,
    np.full_like(theta_circle, r_outer),
    color='black',
    linewidth=2
)

plt.savefig("gauge.svg", bbox_inches="tight")
plt.savefig("gauge.pdf", bbox_inches="tight")
plt.savefig("gauge.png", bbox_inches="tight")
plt.show()
