#!/usr/bin/env python

"""
read a list of points from a CSV file and print out the length of the perimiter of the shape that is formed by joining the points in their listed order
"""

import csv
#added by ayush
import sys

#changed parameters by ayush - previously x0, y1, x1, y1
def get_distance(x1, y1, x2, y2):
    """ use pythagorean theorm to find distance between 2 points """
    a = x1 - x2
    b = y1 - y2
    c_2 = a*a + b*b

    return c_2 ** (1/2)

def get_distances(points):
    """ convert a list of points into a list of distances """
    i = 0
    distances = []
    for i in range(len(points)):
        #condition added by ayush 
        if(0 < i < len(points)-1):
            point = points[i]
            next_point = points[i+1]
            # convert to float before calculation - ayush
            x0 = float(point[0])
            y0 = float(point[1])
            x1 = float(next_point[1])
            y1 = float(next_point[1])
            point_distance = get_distance(x0, y0, x1, y1)
            distances.append(point_distance)
    #added return - ayush
    return distances

def perimiter(points):
    """ returns the length of the perimiter of some shape defined by a list of points """
    distances = get_distances(points)
    length = 0
    for distance in distances:
        length = length + distance

    return length

def main(file_name):

    fp = open(file_name)
    reader = csv.reader(fp)

    points = []
    for row in reader:
        x = row[0]
        y = row[1]
        points.append((x,y))

    length = perimiter(points)

    print length


if __name__ == "__main__":
#changed by ayush - previously sys.argv[0] 
    file_name = sys.argv[1]
    main(file_name)

