
class Node:
    def __init__(self, distance, previous_node, cost):
        self.distance = distance
        self.previous_node = previous_node
        self.cost = cost
        
    def get_distance(self):
        return self.distance
    
    def get_previous_node(self):
        return self.previous_node
    
    def get_cost(self):
        return self.cost
    
    
def task_2(G,Coord,Dist,Cost,start,end):
    from queue import PriorityQueue
    numNodes = 0
    energyBudget = 287931
    nodes = {}
    for i in G:
        nodes[i]= Node(-1, 'NA', 0)
    current_node = start
    dictExplored = {}
    dictExplored[start] = None
    nodes[current_node] = Node(0, 'NA', 0)
  
    q = PriorityQueue()
    q.put([0, current_node])
    
    
    while(not q.empty()):
        current_node = q.get()[1]

        nodes[current_node] = Node(nodes[current_node].distance, nodes[current_node].previous_node, nodes[current_node].cost)
        numNodes += 1
        if(current_node == end):
            break
        
        children = G[current_node]
        for item in children:
                   
            dist = Dist[current_node + "," + item]
            cost = Cost[current_node + "," + item]
            
            newDist = nodes[current_node].distance + dist
            newCost = nodes[current_node].cost + cost

            if(item not in dictExplored or (newDist<nodes[item].distance)):
                if(newCost <= energyBudget):
                    q.put((newDist, item))
                    dictExplored[item] = current_node
                    nodes[item] = Node(newDist, current_node, newCost)
        
    

    current_node = end
    stack = []
    while(current_node != start):
        stack.append(nodes[current_node].previous_node)
        current_node = nodes[current_node].previous_node
        
    print("Shortest path:", end = " ")
    for i in range(len(stack)-1, 0, -1):
        print(stack[i], end ="->")
    print(stack[0], end = "->")
    print(50)

    print("Shortest distance:", end = " ")
    print(nodes[end].distance)

    print("Total energy cost:", nodes[end].cost)
    print("Nodes expanded:", numNodes)
