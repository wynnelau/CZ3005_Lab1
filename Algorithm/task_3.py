def task_3(G, Coord, Dist, Cost):
    start = "1"
    end = "50"
    current_node="1"
    current_energy=0
    current_distance=0
    path=["1"]


    if current_node == end and current_energy<=287932:
        path_string='->'.join([str(elem) for elem in path])
        print("Shortest path: "+path_string+".")
        print("Shortest distance: "+current_distance+".")
        print("Total energy cost: "+current_energy+".")
        return
