import numpy as np

energy = np.array([12, 15, 11, 18, 14, 20, 16])

total_energy = np.sum(energy)
print("Total energy:", total_energy)

average_energy = np.mean(energy)
print("Average energy:", average_energy)

highest_energy = np.max(energy)
print("Highest energy:", highest_energy)

lowest_energy = np.min(energy)
print("Lowest energy:", lowest_energy)

#DAILY ENERGY CONSUMPTION ANALYSIS
for i, day_energy in enumerate(energy):
    percentage_energy = (day_energy / total_energy) * 100
    print(f"Day: {i+1}, Energy: {day_energy}, Percentage of total energy: {percentage_energy:.2f}%")

first_three_days_energy = np.copy(energy[:3])
for i, day_energy in enumerate(first_three_days_energy):
    print(f"Day: {i+1}, Energy: {day_energy}")

over_threshold = []

for day_energy in energy:
    if day_energy > 15:
        print(day_energy, "is above the average energy consumption.")
        over_threshold.append(day_energy)
       
print(f"Days with energy consumption above 15: {len(over_threshold)}")


