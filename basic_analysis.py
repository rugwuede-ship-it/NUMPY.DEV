import numpy as np

energy = np.array([12, 15, 11, 18, 14, 20, 16])
threshold = 15

total_energy = energy.sum()
print("Total energy:", total_energy)
print("Average energy:", energy.mean())
print("Highest energy:", energy.max())
print("Lowest energy:", energy.min())

# Daily energy consumption analysis
percentages = energy / total_energy * 100
for day, (value, pct) in enumerate(zip(energy, percentages), start=1):
    print(f"Day: {day}, Energy: {value}, Percentage of total energy: {pct:.2f}%")

# First three days
for day, value in enumerate(energy[:3], start=1):
    print(f"Day: {day}, Energy: {value}")

# Days above the threshold
over_threshold = energy[energy > threshold]
print(f"Energy values above {threshold}:", over_threshold)
print(f"Days with energy consumption above {threshold}: {len(over_threshold)}")