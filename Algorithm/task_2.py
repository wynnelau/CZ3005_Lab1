
def task_2(G,Coord,Dist,Cost,start,end):
    task2 = task_2_alg(G,Coord,Dist,Cost,start,end)
    Edges = {}
    for y in Cost.keys():
        Edges[y] = Edge(y)
    for y in Edges.values():
        y.set_cost(Cost[y.get_id()])
        y.set_dist(Dist[y.get_id()])
    printPath(task2[1], Edges)


#function to calculate path, distance, energy cost
def task_2_alg(G,Coord,Dist,Cost,start,end):
    from queue import PriorityQueue
    
    budget = 287932
    queue = PriorityQueue()
    visitedSet = set()
    
    
    Nodes = {}
    for x in Coord.keys(): 
        Nodes[x] = Node(x)
    for x in Nodes.values():
        x.set_coord(Coord[x.get_id()][0],Coord[x.get_id()][1])
        x.set_children(G[x.get_id()])
    
    
    Edges = {}
    for y in Cost.keys():
        Edges[y] = Edge(y)
    for y in Edges.values():
        y.set_cost(Cost[y.get_id()])
        y.set_dist(Dist[y.get_id()])
    
    

    startNode = Nodes[start]
    queue.put((0,[startNode.get_id()]))

    while not queue.empty():
        
        current = queue.get()
        objs = current[1]
        nodeCurrent = Nodes[objs[-1]]

        energy = current[0]
        visitedSet.add(nodeCurrent.get_id())

        if len(objs) <= 0:
            continue
        else:
            if (nodeCurrent.get_id() == end):
                return current
            if len(nodeCurrent.get_children()) != 0:
                for item in nodeCurrent.get_children():
                    
                    if not item in visitedSet:
                        childNode = Nodes[item]
                        str = nodeCurrent.get_id() + "," + childNode.get_id()
                        object = Edges[str]
                        energysum = object.get_cost() + energy
                        
                        arr = objs.copy()
                        arr.append(object.get_ToNode())
                        if(energysum < budget):
                            queue.put((energysum, arr))
            
    
    
    return 0

#function to print path
def printPath(arrayPath, Edges):
    
    if(len(arrayPath) > 1):

        distance = 0 
        energysum = 0
        
        edges = 1
        tempPath = arrayPath

        pathString = tempPath[0] + "->"
        while edges < len(tempPath):
            edgeid = tempPath[edges - 1] + "," + tempPath[edges]
            edgeobject = Edges.get(edgeid)
            distance = distance + edgeobject.get_dist()
            energysum = energysum + edgeobject.get_cost()
            if edges == len(tempPath)-1:
                pathString = pathString + tempPath[edges]
            else:
                pathString = pathString + tempPath[edges]  + "->"
            edges+= 1
            #print(pathStr)
        pathString = pathString

        print("Shortest path:",pathString)
        print("Shortest distance:",distance)
        print("Total energy cost:",energysum)
    else:
        pathString = arrayPath[0]
        print("Shortest path:",pathString)
        print("Shortest distance:",0)
        print("Total energy cost:",0)

#############################################################
class Node:
        

        childrenObj = []
        coord = ()
        children = []
        id  = ""

        def __init__(self,id):
            self.id = id

        def get_id(self):
            return self.id

        def set_coord(self, Xpos, Ypos):
            self.coord  = (Xpos,Ypos)
        def get_coord(self):
            return self.coord
        
        def set_children(self,children_list):
            self.children = children_list
        def get_children(self):
            return self.children
        
        



class Edge:    
    cost = 0
    dist = 0
    

    ToObj = None
    
    ToNode = ""
    FromNode = ""
    
    id = ""

    def __init__(self,id):
        self.id = id
        arr = id.split(',')
        self.FromNode = arr[0]
        self.ToNode = arr[1]
        Edges = {}
        
    def get_id(self):
        return self.id
    

    def set_cost(self, cost):
        self.cost = cost
    def get_cost(self):
        return self.cost
    
    def set_dist(self, distance):
        self.dist = distance
    def get_dist(self):
        return self.dist

    def get_FromNode(self):
        return self.FromNode
    def get_ToNode(self):
        return self.ToNode

