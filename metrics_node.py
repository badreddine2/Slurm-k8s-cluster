import matplotlib.pyplot as plt
import numpy as np


from matplotlib.ticker import MaxNLocator

restart_times = [31,30,33,32]
restart_counts = list(range(1, len(restart_times)+1))

plt.figure(figsize=(10, 4))
plt.plot(restart_counts, restart_times, marker='o', linestyle='-', color='b', label='Restarting time')
plt.title("Outage time due to Node failure")
plt.xlabel("Restarts")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylim(0, 60)
plt.show()

