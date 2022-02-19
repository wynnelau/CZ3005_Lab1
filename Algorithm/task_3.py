import math


def task_3(G, Coord, Dist, Cost,start,end):

    nodes={}
    for i in Coord:
        nodes[i]=None
    end_coordinate = Coord[end]
    current_node = "1"
    current_coordinate = Coord[current_node]
    current_energy = 0
    current_distance_travelled = 0
    path = ["1"]
    stack = [start]
    while len(stack) > 0:
        if current_node == end and current_energy <= 287932:
            path_string = '->'.join([str(elem) for elem in path])
            print("Shortest path: " + path_string + ".")
            print("Shortest distance: " + current_distance_travelled + ".")
            print("Total energy cost: " + current_energy + ".")
            return [path_string, current_distance_travelled, current_energy]
        current_node = stack.pop()

        # Look at neighbours
        # list of heuristics
        # find min heuristic
        # add the one with minimum heuristic and loop


def min(a, b):
    if a > b:
        return b
    return a


def max(a, b):
    if b > a:
        return b
    return a


def displacement(a, b):
    displacement_current = math.sqrt(
        (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def evaluation_function(current_distance, b, end):
    return displacement(b, end) + current_distance
