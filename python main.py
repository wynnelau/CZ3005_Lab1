import json


from Algorithm import task_1
from Algorithm import task_2
from Algorithm import task_3



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start='1'
    end='50'
    G = open('G.json')
    G_data = json.load(G)
    Dist = open('Dist.json')
    Dist_data = json.load(Dist)
    Cost = open('Cost.json')
    Cost_data = json.load(Cost)
    Coord = open('Coord.json')
    Coord_data = json.load(Coord)
    # task_1.task_1(G_data,Coord_data,Dist_data,Cost_data,start,end)
    #task_2.task_2(G_data,Coord_data,Dist_data,Cost_data,start,end)
    task_3.task_3(G_data,Coord_data,Dist_data,Cost_data,start,end)


