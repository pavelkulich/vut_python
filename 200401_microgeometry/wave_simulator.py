# zobrazeni fft na harmonickych signalech
import numpy as np
import matplotlib.pyplot as plt

# vytvoreni linearni osy x a frekvencni osy xf
x = np.linspace(0, 0.5 * np.pi, 5000)
xf = np.linspace(0, 1 / (x[1] - x[0]), 8192)

# vypocet funkci sinus
cos1 = np.cos(40 * 2 * np.pi * x) * 3
cos2 = np.cos(90 * 2 * np.pi * x) * 2
cos3 = np.cos(25 * 2 * x * np.pi + 1)
cos_sum = cos1 + cos2 + cos3

# transformace sinu
fft_cos1 = np.fft.fft(cos1)
fft_cos2 = np.fft.fft(cos2)
fft_cos3 = np.fft.fft(cos3)
fft_cos_sum = np.fft.fft(cos_sum)

# vytvoreni poli pro doplnovani hodnot ve smycce for
sins = np.array([cos1, cos2, cos3, cos_sum])
fft_sins = np.array([fft_cos1, fft_cos2, fft_cos3, fft_cos_sum])
texts = ['cos(40*2*Pi*x)*3', 'cos(90*2*Pi*x)*2', 'cos(25*2*Pi*x+1)',
         'cos(40*2*Pi*x)*3 + cos(90*2*Pi*x)*2 + cos(25*2*Pi*x+1)']
colors = ['blue', 'blue', 'blue', 'red']

# vytvoreni grafu
fig = plt.figure()
for i in range(sins.shape[0]):
    plt.subplot(sins.shape[0], 2, 2 * i + 1, xmargin=0)
    plt.plot(x, sins[i], color=colors[i])
    plt.title(f'{texts[i]}', fontsize=15)
    plt.ylim(-6, 6)

    if i == sins.shape[0] - 1:
        plt.xlabel('Čas [s]')

    plt.ylabel('Amplituda [-]')
    plt.grid()
    plt.subplot(sins.shape[0], 2, 2 * i + 2, xmargin=0)
    plt.plot(xf[0:xf.size // 2], np.abs(fft_sins[i][0:xf.size // 2]) / xf.shape[0], color=colors[i])
    plt.xscale('log')
    plt.ylim(0, 1.6)

    if i == sins.shape[0] - 1:
        plt.xlabel('Frekvence [Hz]')

    plt.title(f'FFT({texts[i]})', fontsize=15)
    plt.grid()

plt.subplots_adjust(wspace=0.1, hspace=0.37)
plt.show()
