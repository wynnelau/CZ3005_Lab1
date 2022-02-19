import math


def displacement(a, b):
    displacement_current = math.sqrt(
        (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return displacement_current


class Node:
    def __init__(self, distance_travelled, energy_cost, visited, previous_node, coord1, coord2,
                 neighbours):
        self.displacement = displacement(coord1, coord2)
        self.neighbours = neighbours
        self.visited = visited
        self.previous_node = previous_node
        self.energy_cost = energy_cost
        self.distance_travelled = distance_travelled
        self.heuristic = 999999999999

    def update_node(self, distance_travelled, energy_cost, previous_node):
        if (energy_cost + self.displacement) < self.heuristic or self.visited == False:
            self.energy_cost = energy_cost
            self.heuristic = energy_cost + self.displacement
            self.visited = True
            self.previous_node = previous_node
            self.distance_travelled = distance_travelled

    def get_neighbour(self):
        return self.neighbours

    def get_heuristic(self):
        return self.heuristic

    def get_previous_node(self):
        return self.previous_node

    def get_distance_travelled(self):
        return self.distance_travelled

    def visited(self):
        return self.visited

    def get_energy_cost(self):
        return self.energy_cost


def task_3(G, Coord, Dist, Cost, start, end):
    nodes = {}

    for i in Coord:
        nodes[i] = Node(0, 0, False, "No node", Coord[i], Coord[end], G[i])
    # initialize
    current_node = start
    stack_node = [current_node]
    stack_heuristic = [nodes[current_node].get_heuristic()]
    nodes[current_node].update_node(0, 0, start)

    while len(stack_node) > 0:
        temp_neighbour = nodes[current_node].get_neighbour()
        for i in temp_neighbour:
            string_pair = ','.join([i, current_node])
            distance_successor = Dist[string_pair] + nodes[current_node].get_distance_travelled()
            energy_successor = Cost[string_pair] + nodes[current_node].get_energy_cost()
            nodes[i].update_node(distance_successor, energy_successor, current_node)
            stack_node.append(i)
            stack_heuristic.append(nodes[i].get_heuristic())
        # if current node is goal node
        if current_node == end and 0 < nodes[current_node].get_heuristic() <= 287932:
            path_string = ["50"]
            previous_node = nodes[current_node].get_previous_node()
            while (nodes[previous_node] != "1"):
                path_string.insert(0, previous_node)
                previous_node = nodes[previous_node].get_previous_node()
            path_string.insert(0, "1")
            path_string_actual = '->'.join([str(elem) for elem in path_string])
            print("Shortest path: " + path_string_actual + ".")
            print("Shortest distance: " + nodes[current_node].get_distance_travelled() + ".")
            print("Total energy cost: " + nodes[current_node].get_energy_cost() + ".")
            return [path_string, nodes[current_node].get_distance_travelled(), nodes[current_node].get_energy_cost()]

        # if not goal node
        minimum_heuristic = min(stack_heuristic)
        min_index = stack_heuristic.index(minimum_heuristic)
        minimum_heuristic = stack_heuristic.pop(min_index)
        current_node = stack_node.pop(min_index)


        # Look at neighbours
        # list of heuristics
        # find min heuristic
        # add the one with minimum heuristic and loop
