import numpy as np

# Define the robot's world in (X, Y, Z) coordinates
# X = Forward, Y = Left/Right, Z = Altitude
robot_start = np.array([0, 0, 0])
target_goal = np.array([6, 8, 0])

# Calculate the Vector (The path from A to B)
path_vector = target_goal - robot_start

# Calculate the Euclidean Distance (The straight-line length)
# This is basically the 3D version of the Pythagorean theorem
distance = np.linalg.norm(path_vector)

print(f"--- Navigation Logic ---")
print(f"Robot starting point: {robot_start}")
print(f"Target destination:  {target_goal}")
print(f"Vector to follow:    {path_vector}")
print(f"Total distance:      {distance:.2f} meters")