import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

restart_times = [19, 34, 49, 93]
restart_counts = list(range(1, len(restart_times)+1))

plt.figure(figsize=(10, 4))
plt.plot(restart_counts, restart_times, marker='o', linestyle='-', color='b', label='Restarting time')
plt.title("Outage time due to Pod failure")
plt.xlabel("Restarts")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)

# Utiliser MaxNLocator pour forcer les valeurs de l'axe x à être des entiers
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()