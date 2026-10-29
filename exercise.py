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
for i, energy in enumerate(energy):
    percentage_energy = (energy / total_energy) * 100
    print(f"Day: {i+1}, Energy: {energy}, Percentage of total energy: {percentage_energy:.2f}%")
    

