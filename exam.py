import math

points = [(1, 5), (2, 7), (1, 6), (4, 3), (3, 8), (2, 7), (1, 2), (3, 4)]

def eucledianDistance(x, y):
    xp = x[0] - y[0]
    yp = x[1] - y[1]
    return math.sqrt((xp * xp) + (yp * yp))

centroid = [(1.8, 6.6), (3.5, 3.5), (1, 2)]
for i in points:
    print(i, " -> ", end="")
    for j in centroid:
        print(eucledianDistance(i, j), end= " ")
    print()