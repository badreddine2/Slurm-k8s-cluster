import matplotlib.pyplot as plt
import numpy as np

restart_times = [32,31 ,30,33,32]
restart_counts = list(range(0, len(restart_times)))

mean_time = np.mean(restart_times)

plt.figure(figsize=(10, 5))
plt.plot(restart_counts, restart_times, marker='o', linestyle='-', color='b', label='Restarting time')
plt.axhline(y=mean_time, color='r', linestyle='--', label=f'Average = {mean_time} secondes')

plt.title("Outage time due to Node failure")
plt.xlabel("Restarts")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
