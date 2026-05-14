import numpy as np, matplotlib.pyplot as plt
from pathlib import Path

def smooth(x, w=10):
    c = np.cumsum(np.insert(x, 0, 0))
    s = c[w:] - c[:-w]
    return np.concatenate([c[1:w] / np.arange(1, w), s / w])[:len(x)]

input_folder = Path('signals')
output_folder = input_folder / 'filtered_plots'
output_folder.mkdir(exist_ok=True)

for f in input_folder.glob('signal*.dat'):
    d = np.loadtxt(f)
    sd = smooth(d)
    plt.plot(d, alpha=0.7, label='raw')
    plt.plot(sd, label='smoothed')
    plt.legend(), plt.grid(), plt.title(f.stem)
    plt.savefig(output_folder / f'{f.stem}_filtered.png')
    plt.close()