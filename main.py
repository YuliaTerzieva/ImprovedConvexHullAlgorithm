import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint
from numpy.random import choice

# --------------- Initialization of Points Sets ---------------#
CrossingCoord = [(500, 100), (500, 6200), (10000, 6200), (10000, 100), (4350, 6201), (5220, 6203), (6120, 6202),
                 (8000, 6201), (5200, 4000), (5200, 4500), (5200, 5000), (5200, 5500), (5200, 6000), (6210, 4245)]

PlaiserTakCoord = [(750, 500), (4500, 500), (8250, 500), (4500, 1125), (4500, 1750), (4500, 2375), (4500, 3000),
                   (4500, 3625), (750, 5500), (8250, 5500)]

WorkCoordinates = CrossingCoord

# --------------- Step 1 : Boundary Points Initialization ---------------#
x_min = (min(WorkCoordinates, key=lambda t: t[0]))[0]
x_max = (max(WorkCoordinates, key=lambda t: t[0]))[0]
y_min = (min(WorkCoordinates, key=lambda t: t[1]))[1]
y_max = (max(WorkCoordinates, key=lambda t: t[1]))[1]
print('The boundaries are bottom left({}, {}), top left({}, {}), top right({}, {}), bottom right({}, {})'.format(
    x_min, y_min, x_min, y_max, x_max, y_max, x_max, y_min))


# --------------- Step 2 : Selection of Starting Point and Direction ---------------#

rand = randint(0, len(WorkCoordinates) - 1)
startPoint = WorkCoordinates[rand]

# Suggestion - We can represent the connections/arcs between points with a matrix N by N with N being the number of
# points. If there is a connection with those points we put a 1, otherwise 0. We need to keep track of which points
# are added to the path and which are not. Another idea is to create a class where every point would have a left
# neightbour and a right one. That would be more time consuming tho.