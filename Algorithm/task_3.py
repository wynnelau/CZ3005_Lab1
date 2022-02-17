import math

def task_3(G, Coord, Dist, Cost):
    start = "1"
    end = "50"
    end_coordinate=Coord[end]
    current_node = "1"
    current_coordinate=Coord[current_node]
    current_energy = 0
    current_distance = 0
    path = ["1"]
    displacement_current=math.sqrt((current_coordinate[0]-end_coordinate[0])**2+(current_coordinate[1]-end_coordinate[1])**2)
    while True:
        #Look at neighbours
        #list of heuristics
        #find min heuristic
        #add the one with minimum heuristic and loop

        if current_node == end and current_energy <= 287932:
            path_string = '->'.join([str(elem) for elem in path])
            print("Shortest path: " + path_string + ".")
            print("Shortest distance: " + current_distance + ".")
            print("Total energy cost: " + current_energy + ".")
            return
