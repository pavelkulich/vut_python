# vizualizace vzorkovaci frekvence
import numpy as np
import matplotlib.pyplot as plt

# vytvoreni datovych vektoru
x = np.linspace(0, 10 * np.pi, 1000)
y = np.sin(x)

# pole nasobku pi pro upraveni f_vz
consts = [2.1, 1, 0.2]

# smycka pro vypocet a vykresleni 3 datovych rad
for i in range(3):
    f_x = []
    f_y = []
    idx = 1
    f = 1

    # vypocet dilcich vektoru pro vzorkovani
    while f < np.max(x):
        f_x.append(f)
        f_y.append(np.sin(f))
        f += consts[i] * np.pi
        idx += 1

    # vykresleni grafu
    plt.subplot(3, 1, i + 1)
    plt.plot(x, y)
    plt.scatter(f_x, f_y, color='red')
    plt.plot(f_x, f_y)
    comment = ''
    if consts[i] == 1:
        comment = ' ... Nyquistova frekvence'
    plt.title(f'f_max = {consts[i] / 2} * f_vz{comment}', fontsize=15)
    plt.grid()

    if i == 2:
        plt.xlabel('Čas [s]')

    plt.ylabel('Amplituda [-]')

plt.subplots_adjust(hspace=0.37)
plt.show()
