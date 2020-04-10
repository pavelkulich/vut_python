# Vypocet a zobrazeni fft pro vsechny datove sloupce
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# nacteni dat
data = pd.read_csv('data/micro.txt', sep=';')

analyzed_samples = 4000
fft_all = []
data_all = []
t = data['x'][1] - data['x'][0]
x = data['x'][0:analyzed_samples]
xf = np.linspace(0, 1/t, x.shape[0])

columns = data.columns[1::]

for column in columns:
    col_fft = np.fft.fft(data[column][0:analyzed_samples])
    fft_all.append(col_fft)
    data_all.append(data[column][0:analyzed_samples])

i = 0
# vykresleni grafu
fig = plt.figure()
for i in range(len(data_all)):
    plt.subplot(len(data_all), 2, 2 * i + 1, xmargin=0)
    plt.plot(x, data_all[i], color='red')
    plt.title(f'Pásmo {columns[i]}', fontsize=15)

    if i == len(data_all) - 1:
        plt.xlabel('Staničení [m]')

    plt.ylabel('Amplituda [-]')
    plt.grid()
    plt.subplot(len(fft_all), 2, 2 * i + 2, xmargin=0)
    plt.plot(xf[:xf.size // 2], np.abs(fft_all[i][:xf.size // 2]) / xf.shape[0])
    plt.title(f'FFT pásma {columns[i]}', fontsize=15)
    plt.xscale('log')
    plt.xlim(0.1, 100)

    if i == len(fft_all) - 1:
        plt.xlabel('Četnost vzorků [1/m]')

    plt.grid()

plt.subplots_adjust(wspace=0.1, hspace=0.37)
plt.show()
