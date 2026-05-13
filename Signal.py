import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def smooth(data, w=10):
    res = np.zeros_like(data)
    for i in range(len(data)):
        res[i] = np.mean(data[max(0, i-w+1):i+1])
    return res

folder = Path("signals")
for f in folder.glob("signal*.dat"):
    raw = np.loadtxt(f)
    filtered = smooth(raw)
    plt.plot(raw, alpha=0.5, label="raw")
    plt.plot(filtered, label="smoothed")
    plt.legend()
    plt.title(f.name)
    plt.savefig(folder / f"{f.stem}_filtered.png")
    plt.close()
    print(f"{f.name} done")