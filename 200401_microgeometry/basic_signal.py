# vizualizace harmonickeho signalu
import numpy as np
import matplotlib.pyplot as plt

# vytvoreni datovych vektoru
x = np.linspace(-1, 2 * np.pi - 1, 1000)
y = np.sin(x + 1)

# vykresleni grafu
plt.plot(x, y, linewidth=3, label='C*cos(2*pi/T+phi)')
plt.plot([np.pi / 2 - 1, np.pi / 2 - 1], [0, 1], linewidth=6, label='Amplituda C')
plt.plot([-1, 2 * np.pi - 1], [0, 0], linewidth=10, label='Petioda T')
plt.plot([-1, 0], [0, 0], linewidth=4, label='Fázový posun phi')
plt.plot([0, 0], [-1.2, 1.2], color='black')
plt.ylim(-1.2, 1.2)
plt.xlabel('Čas [s])', fontsize=20)
plt.xticks(fontsize=15)
plt.ylabel('Amplituda [-])', fontsize=20)
plt.yticks(fontsize=15)
plt.legend(fontsize=30)
plt.grid()
plt.show()
