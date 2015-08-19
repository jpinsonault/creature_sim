from math import sqrt


def get_bounding_square(points):
    max_radius = get_bounding_circle(points)
    return (-max_radius, -max_radius, max_radius * 2, max_radius * 2)


def get_bounding_circle(points):
    greatest_distance = 0
    for point in points:
        distance = point[0]**2 + point[1]**2
        greatest_distance = max(distance, greatest_distance)

    # Return the radius of the bounding circle
    return sqrt(greatest_distance)
