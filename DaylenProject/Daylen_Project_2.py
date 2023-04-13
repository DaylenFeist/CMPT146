#BASED ON https://cargocollective.com/sagejenson/physarum
from PIL import Image
import numpy as np

WIDTH = 1000
HEIGHT = 1000
move_speed = 1


# allows for the creation of many agent objects
class agent_class:
    # initialize all starting variables, will allow for variation in position & rotation
    def __init__(self, pos_x, pos_y, rotation):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = rotation

    # move forward

    def move_agent(self):
        # will have to add checks to make sure the agent hasnt gone past the edge!
        self.pos_x = self.pos_x + np.sin(self.rotation)
        self.pos_y = self.pos_y + np.cos(self.rotation)
        if self.pos_x >= WIDTH or self.pos_x <= 0:
            self.rotation += np.pi / 2

    # possibly add a sniff fuction to turn towards trails
    # for debug purposes

    def __str__(self):
        return f"x:{self.pos_x} | y:{self.pos_y} | rotation: {self.rotation}"


def update_background(background, list_of_agents):
    for agent in agents:
        background[int(round(agent.pos_x, 0)), int(round(agent.pos_y, 0))] = 255
    return background

# Create the frames
frames = []
agents = []
agents.append(agent_class(1,6,0))
agents.append(agent_class(1,6,-1))
agents.append(agent_class(1,6,-2))
agents.append(agent_class(1,6,-3))


background = np.zeros((WIDTH, HEIGHT), dtype=np.uint8)

for i in range(500):
    for agent in agents:
        agent.move_agent()
    background = update_background(np.copy(background), agents)
    frames.append(Image.fromarray(background))

# Save into a GIF file that loops forever
frames[0].save('background.gif', format='GIF', append_images=frames[1:], save_all=True, fps=60, loop=0)
im1 = frames[1].save('last_frame.jpg')

im1 = frames[2].save('last_frame2.jpg')