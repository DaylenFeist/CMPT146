# BASED ON https://cargocollective.com/sagejenson/physarum

"""
Author: Daylen Feist
Created: 2023-04-13

"""
from PIL import Image
import numpy as np
import random

WIDTH = 500
HEIGHT = 500
MOVE_SPEED = 1
FRAMES = 500
NUM_AGENTS = 1000

SNIFF_ANGLE = np.pi / 8
SNIFF_LENGTH = 1


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
        self.pos_x = self.pos_x + MOVE_SPEED * np.cos(self.rotation)
        self.pos_y = self.pos_y + MOVE_SPEED * np.sin(self.rotation)

        # make better this sucks

        if self.pos_x >= WIDTH - .5:
            self.pos_x -= WIDTH
        if self.pos_x < 0:
            self.pos_x += WIDTH - .5

        if self.pos_y >= HEIGHT -.5:
            self.pos_y -= HEIGHT
        if self.pos_y < 0:
            self.pos_y += HEIGHT - .5

    # possibly add a sniff fuction to turn towards trails
    def sniff(self, trail_map):
        # sniffs in three directions
        # these bois are long, maybe make this better

        # probably a better way to do this, will explore options in the future!!!!!
        left_sniff = check_square(trail_map, self, SNIFF_ANGLE, SNIFF_LENGTH)
        right_sniff = check_square(trail_map, self, -SNIFF_ANGLE, SNIFF_LENGTH)

        # change out of uint8
        turn_weight = (int(left_sniff) - int(right_sniff)) * SNIFF_ANGLE *2 / 255

        # make sure rotation doesnt get too big or too small
        self.rotation += turn_weight
        if self.rotation > np.pi * 2:
            self.rotation -= np.pi * 2
        if self.rotation < 0:
            self.rotation += np.pi * 2

    # for debug purposes
    def __str__(self):
        return f"x:{self.pos_x} | y:{self.pos_y} | rotation: {self.rotation}"


def check_square(trail_map, agent, angle, distance):
    """
    Purpose: Check the brightness of a square on the trail_map, and if it is on the outside, return 0
    but might want to change that
    """
    #find point forwards
    square_x = int(round(agent.pos_x + distance * np.cos(agent.rotation + angle), 0))
    square_y = int(round(agent.pos_y + distance * np.sin(agent.rotation + angle), 0))
    if square_x >= WIDTH or square_x < 0 or square_y >= HEIGHT or square_y < 0:
        square_brightness = 0
    else:
        square_brightness = trail_map[square_x, square_y]
    return square_brightness


def update_trail_map(trail_map, list_of_agents):
    """
    Purpose:
        Function updates the trail_map, by adding agent trails, darkening the trail_map, and diffusing it.
    Pre-Condition:
        trail_map: numpy 2D array
        list_of_agents: list of agents, each agent must have position within the bounds of the numpy array

    Post-Condition:
        None
    Return:
        trail_map after these alterations
    """
    for agent in agents:
        # Each Agent releases a trail which is
        trail_map[trail_map >= 205] = 205
        trail_map[int(round(agent.pos_y, 0)), int(round(agent.pos_x, 0))] += 50
    # We want to also diffuse
    # and darken the trail_map over time

    trail_map[trail_map <= 5] = 5
    trail_map -= 5
    return trail_map


# initialize the agents
agents = []
# create agents with different presets
for x in range(NUM_AGENTS):
    agents.append(agent_class(random.randint(25, 75), random.randint(25, 75), random.random() * np.pi * 2))

# create the trail map to specficiations
trail_map = np.zeros((WIDTH, HEIGHT),dtype=np.uint8)
# using uint 8 as we only need black and white, might play around with this in the future

# Create the frames
frames = []
for i in range(FRAMES):
    progress = i/FRAMES * 100
    print(f"{round(progress,1)}%")
    # update all agents
    for agent in agents:
        agent.move_agent()
        agent.sniff(trail_map)
        # print(agent.__str__())

    # update the trail map
    # Used np.copy as it was creating issues with referencing
    trail_map = update_trail_map(np.copy(trail_map), agents)

    # use PIL to convert to an image object, and add that to the frames
    frames.append(Image.fromarray(trail_map))

# Save into a GIF file that loops forever
# FOR FUTURE CONSIDERATION, CHANGING FRAMERATE AND OTHER PROPERTIES
frames[0].save('trail_map.gif', format='GIF', append_images=frames[1:], save_all=True, fps=60, loop=0)
