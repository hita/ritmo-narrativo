import matplotlib.pyplot as plt
import numpy as np

def ritmo_narrativo_crimen_y_castigo(tiempo):
    if tiempo <= 0.25:
        return 0.1 * tiempo
    elif tiempo <= 0.5:
        return 0.4
    elif tiempo <= 0.75:
        return 0.6 * tiempo - 0.15
    else:
        return -0.4 * tiempo + 1.4

def ritmo_narrativo_la_metamorphosis(tiempo):
    if tiempo <= 0.25:
        return 0.2 * tiempo
    elif tiempo <= 0.5:
        return -0.1 * tiempo + 0.35
    elif tiempo <= 0.75:
        return 0.15 * tiempo - 0.05
    else:
        return -0.2 * tiempo + 1

time = np.linspace(0, 1, 100)

plt.plot(time, [ritmo_narrativo_crimen_y_castigo(t) for t in time], label='Crimen y Castigo')
plt.plot(time, [ritmo_narrativo_la_metamorphosis(t) for t in time], label='La Metamorphosis')
plt.xlabel('Time')
plt.ylabel('Ritmo Narrativo')

# Add labels for the change of narrative rhythm

# Add labels for key moments
plt.annotate("Raskolnikov's confession", xy=(0.5, ritmo_narrativo_crimen_y_castigo(0.5)), xytext=(0.5, 0.6),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.01))

plt.annotate("Raskolnikov's arrest", xy=(0.75, ritmo_narrativo_crimen_y_castigo(0.75)), xytext=(0.5, 0.8),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.01))


plt.annotate("Raskolnikov's imprisonment", xy=(0.9, ritmo_narrativo_crimen_y_castigo(0.9)), xytext=(0.9, 0.1),
            arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.01))
plt.annotate("Raskolnikov's redemption", xy=(0.95, ritmo_narrativo_crimen_y_castigo(0.95)), xytext=(0.95, 0.4),
            arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.01))

plt.annotate("Raskolnikov's trial", xy=(1, ritmo_narrativo_crimen_y_castigo(1)), xytext=(1, 0.6),
            arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.01))



plt.annotate("Gregor's transformation", xy=(0.25, ritmo_narrativo_la_metamorphosis(0.25)), xytext=(0.05, 0.8),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))

plt.annotate("Gregor's isolation", xy=(0.5, ritmo_narrativo_la_metamorphosis(0.5)), xytext=(0.34, 0.78),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))

plt.annotate("Family's plan to move", xy=(0.8, ritmo_narrativo_la_metamorphosis(0.8)), xytext=(0.8, 0.5),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))


plt.annotate("Family's acceptance of Gregor's death", xy=(0.9, ritmo_narrativo_la_metamorphosis(0.9)), xytext=(0.6, 1.05),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))

plt.annotate("Family's financial improvement", xy=(0.95, ritmo_narrativo_la_metamorphosis(0.95)), xytext=(0.7, 1.0),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))

plt.annotate("Gregor's death", xy=(1, ritmo_narrativo_la_metamorphosis(1)), xytext=(0.9, 1.05),
             arrowprops=dict(facecolor='black', width=0.5, headwidth=6, shrink=0.05))

plt.legend()
plt.show()
