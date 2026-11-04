import numpy as np

sensor_A = np.array([22, 24, 23, 27, 26])
sensor_B = np.array([21, 25, 23, 25, 28])
threshold = 2

differences = np.abs(sensor_A - sensor_B)
print("Temperature differences:", differences)

print("Mean of Sensor A:", np.mean(sensor_A))
print("Mean of Sensor B:", np.mean(sensor_B))

large_diffs = differences[differences > threshold]
print(f"Differences above {threshold} degrees:", large_diffs)