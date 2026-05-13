import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

f = "3.dat"
if not Path(f).exists():
    f = "../3.dat"

u = np.loadtxt(f)
fig, ax = plt.subplots()
line, = ax.plot(u)
ax.grid(True)

def update(t):
    global u
    if t:
        u = (u + np.roll(u, 1)) / 2
    line.set_ydata(u)
    ax.set_title(t)

ani = FuncAnimation(fig, update, frames=256, interval=50)
ani.save("wave.gif", writer="pillow")