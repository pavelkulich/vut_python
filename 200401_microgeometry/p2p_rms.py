# vypocteni rms nebo p2p pro vsechny datove sloupce
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# funkce pro vypocitani rms
def calculate_rms(data):
    rms = np.sqrt(np.mean(data ** 2))
    return rms


# funkce pro vypocitani p2p
def calculate_p2p(data):
    p2p = np.ptp(data)
    return p2p


what_to_calculate = 'p2p'  # 'p2p nebo 'rms'

# velikosti okenek pro jednotliva vlnova pasma
wave_len = {'p1': 0.150,
            'p2': 0.500,
            'p3': 1.500,
            'p4': 5.000}

# nacteni dat
data = pd.read_csv('data/micro.csv', sep=';')

# osa x
x = data['x']

# interval mezi vzorky
t = x[1] - x[0]

columns = data.columns[1::]

mean_list = []
windows = []

# smycka pro vytvoreni okenka pro jednotliva vlnova pasma
for key in wave_len:
    window = int(wave_len[key] / t)
    windows.append(window)
    column_mean = []

    # smycka pro vypocet "prumeru" na zaklade velikosti okenka
    for i in range(data[key].size - window):
        data_window = data[key][i:window + i]

        if what_to_calculate == 'p2p':
            mean = calculate_p2p(data_window)
        elif what_to_calculate == 'rms':
            mean = calculate_rms(data_window)
        else:
            break

        column_mean.append(mean)
    mean_list.append(column_mean)

idx = 1
# smycka pro vizualizaci dat
for p2p_idx in range(len(mean_list)):
    plt.subplot(4, 2, 2 * idx - 1, xmargin=0)
    plt.plot(x, data[columns[idx - 1]])
    plt.title(f'Pásmo {columns[idx - 1]}', fontsize=18)
    plt.ylim(-0.00014, 0.00014)

    if idx == len(mean_list):
        plt.xlabel('Staničení [m]', fontsize=13)

    plt.grid()

    plt.subplot(4, 2, 2 * idx, xmargin=0)
    plt.plot(data['x'][0:data['x'].shape[0] - windows[p2p_idx]], mean_list[p2p_idx])
    plt.title(f'{what_to_calculate} pro pásmo {columns[idx - 1]}', fontsize=18)
    plt.ylabel('Amplituda [mm]', fontsize=13)

    if idx == len(mean_list):
        plt.xlabel('Staničení [m]', fontsize=13)

    plt.ylim(0, 0.0003)
    plt.grid()

    idx += 1

plt.subplots_adjust(wspace=0.2, hspace=0.35)
plt.show()
