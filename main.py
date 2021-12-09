# Coordinates of all points, this is for the crossing grid
coords = [(500, 100), (500, 6200), (10000, 6200), (10000, 100), (4350, 6201), (5220, 6203), (6120, 6202), (8000, 6201),
          (5200, 4000), (5200, 4500), (5200, 5000), (5200, 5500), (5200, 6000), (6210, 4245)]

# Setting minimum and maximum values for the boudaries
x_min = y_min = 9999999
x_max = y_max = 0

# Plot the points
for c in coords:
    plt.scatter(c[0], c[1])

    if c[0] < x_min:
        x_min = c[0]
    if c[0] > x_max:
        x_max = c[0]
    if c[1] < y_min:
        y_min = c[1]
    if c[1] > y_max:
        y_max = c[1]

# Invert the y axis to represent the grid on the site equally
plt.gca().invert_yaxis()

print(x_min, x_max, y_min, y_max)

print(len(coords))

# Select a random starting point
rand = randint(0, len(coordinates) - 1)
print(rand)
start = coords[rand]
print(start)