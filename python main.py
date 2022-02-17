import json






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    G = open('G.json')
    G_data = json.load(G)
    Dist = open('Dist.json')
    Dist_data = json.load(Dist)
    Cost = open('Cost.json')
    Cost_data = json.load(Cost)
    Coord = open('Coord.json')
    Coord_data = json.load(Coord)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
