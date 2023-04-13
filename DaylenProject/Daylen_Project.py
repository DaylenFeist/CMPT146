"""
This file will be used to prototype my project for this class
"""
# Importing the required modules
import numpy as np
import matplotlib.pyplot as plt

#create ball object
class agent:
    def __init__(self, pos_x, pos_y, rotation):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = rotation

    def __str__(self):
        return f"x:{self.pos_x} | y:{self.pos_y} | rotation: {self.rotation}"


agent_1 = agent(6,6,0)
print(agent_1)


# Generating data for the heat map
data = np.ones((12,12))

# Function to show the heat map
plt.imshow(data, cmap='magma')

# Adding details to the plot
plt.title("2-D Heat Map")
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Adding a color bar to the plot
plt.colorbar()

# Displaying the plot
plt.show()
