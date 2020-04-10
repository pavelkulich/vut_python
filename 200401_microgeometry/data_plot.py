# vizualizace dat vsech datovych sloupcu
import pandas as pd
import matplotlib.pyplot as plt

# nacteni dat
data = pd.read_csv('data/micro.txt', sep=';')

# vytvoreni pole od indexu 1 do konce (vybechani prvniho sloupce)
# hodnoty jsou doplnovany do popisku grafu
columns = data.columns[1::]

# promenna pro indexaci subplotu ve smycce
idx = 1

# vytvoreni grafu
fig = plt.figure()
fig.suptitle('Mikrogeometrie ve vlnových pásmech p1 - p4', fontsize=30, y=1)
for column in columns:
    plt.subplot(2, 2, idx, xmargin=0)
    plt.plot(data['x'][0:4000], data[column][0:4000])
    plt.title(f'Pásmo {column}', fontsize=18)
    plt.xlabel('Staničení [m]', fontsize=13)
    plt.ylabel('Amplituda [mm]', fontsize=13)
    plt.grid()

    idx += 1

plt.tight_layout()
plt.subplots_adjust(wspace=0.15, hspace=0.30)
plt.show()
