import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint
from scipy.spatial import distance
from numpy.random import choice

# --------------- Initialization of Points Sets ---------------#
CrossingCoord = [(500, 100), (500, 6200), (10000, 6200), (10000, 100), (4350, 6201), (5220, 6203), (6120, 6202),
                 (8000, 6201), (5200, 4000), (5200, 4500), (5200, 5000), (5200, 5500), (5200, 6000), (6210, 4245)]

PlaiserTakCoord = [(750, 500), (4500, 500), (8250, 500), (4500, 1125), (4500, 1750), (4500, 2375), (4500, 3000),
                   (4500, 3625), (750, 5500), (8250, 5500)]

SShaped = [(893, 2114), (4513, 3711), (4878, 3453), (5213, 3179), (5578, 2905), (928, 2631), (6232, 2418),
           (6628, 2099), (6993, 1840), (7342, 1764), (7707, 1840), (7966, 2069)]

Dantzig = [(2100, 600), (6900, 5400), (5700, 4200), (4500, 3000), (5700, 3000), (6300, 3000), (6900, 3000),
           (3300, 1800), (2100, 5400), (6900, 600)]
SmallExample = [(10, 10), (20, 20), (30, 25), (40, 25), (80, 60), (90, 70), (97, 77), (100, 80), (40, 90)]

WorkCoordinates = SmallExample

# --------------- Our algorithm good continuation ---------------#
def distancePointFromLine(point1L, point2L, point):
    x1 = point1L[0]
    y1 = point1L[1]
    x2 = point2L[0]
    y2 = point2L[1]
    x0 = point[0]
    y0 = point[1]
    topPart = abs((x2 - x1)*(y1-y0) - (x1 - x0)*(y2-y1))
    bottomPart = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return topPart/bottomPart


def getPathsGivenStartingPoint(Points, startingPointIndex, maxDistance, distances) :
    ClosestPointDistance = min(distances[startingPointIndex])
    ClosestPointIndex = distances[startingPointIndex].index(ClosestPointDistance)

    list = []
    list.extend([startingPointIndex, ClosestPointIndex])
    while ClosestPointDistance < maxDistance :
        distancesRest = [(distancePointFromLine(Points[startingPointIndex], Points[ClosestPointIndex], Points[i]), i)
                         if i not in list else (maxDistance+1, -1) for i in range(len(Points))]
        distancesRestMin = min(distancesRest, key = lambda t: t[0])
        if distancesRestMin[0] < maxDistance :
            list.append(distancesRestMin[1])
            ClosestPointDistance = distancesRestMin[0]
            ClosestPointIndex = distancesRestMin[1]
        else :
            return list
    return list.sort()


def getAllSets(Points, minNumberElement, maxDistance):
    allLists = []
    distances = [[distance.euclidean(a, b) for a in WorkCoordinates] for b in WorkCoordinates]
    for startingPointIndex in range(len(Points)) :
        list = getPathsGivenStartingPoint(Points, startingPointIndex, maxDistance, distances)
        if len(list) >= minNumberElement :
            if list not in allLists :
                allLists.append(list)
    return allLists

print(getAllSets(WorkCoordinates, 3, 5))
# --------------- Slopes between lines algorithm ---------------#
# slopes = np.array([[(a[1] - b[1]) / (a[0] - b[0]) if a[0] != b[0] else None for a in WorkCoordinates]
#                    for b in WorkCoordinates])
#
# distances = np.array([[math.dist(a, b) for a in WorkCoordinates]
#                       for b in WorkCoordinates])
# # print(slopes)
# # print(distances)
#
# maxDifference = 0.001
# minElements = 3
# maxDist = 3
#
# groups = []
# for i, row in enumerate(slopes):
#     similar = []
#     for j in range(len(WorkCoordinates)):
#         similarInt = []
#         for k in range(len(WorkCoordinates)):
#             if j != k and slopes[i][j] is not None and slopes[j][k] is not None:
#                 if abs(slopes[i][j] - slopes[j][k]) < maxDifference:
#                     similarInt.append(k)
#         if len(similarInt) > minElements - 1:
#             similarInt.append(j)
#             if similarInt.sort() not in similar:
#                 similar.append(similarInt.sort())
#     groups.append(similar)
#
# for g in groups:
#     print(g)

# # --------------- Step 1 : Boundary Points Initialization ---------------#
# x_min = (min(WorkCoordinates, key=lambda t: t[0]))[0]
# x_max = (max(WorkCoordinates, key=lambda t: t[0]))[0]
# y_min = (min(WorkCoordinates, key=lambda t: t[1]))[1]
# y_max = (max(WorkCoordinates, key=lambda t: t[1]))[1]
# # print('The boundaries are bottom left({}, {}), top left({}, {}), top right({}, {}), bottom right({}, {})'.format(
# #     x_min, y_min, x_min, y_max, x_max, y_max, x_max, y_min))
#
# distances = np.array([[distance.euclidean(a, b) for a in WorkCoordinates] for b in WorkCoordinates])
# # print(distances)
#
# average = distances.mean()
# # print(average)
#
# cluster = []
# for i, row in enumerate(distances):
#     if (row.mean() < average):
#         cluster.append(WorkCoordinates[i])
#
# print(cluster)
# # --------------- Step 2 : Selection of Starting Point and Direction ---------------#
#
# rand = randint(0, len(WorkCoordinates) - 1)
# startPoint = WorkCoordinates[rand]
