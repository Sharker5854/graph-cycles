from pprint import pprint
from graph import Graph
from utils import trans_matrix_to_list, find_all_cycles

arc_matrix = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0]
]
graph = Graph(arc_list=trans_matrix_to_list(arc_matrix))

# graph = Graph()

# graph.add_ver("A", 0)
# graph.add_ver("B", 1)
# graph.add_ver("C", 2)
# graph.add_ver("D", 3)
# graph.add_ver("E", 4)

# graph.add_arc(0, 1, 1)
# graph.add_arc(0, 2, 1)
# graph.add_arc(0, 3, 1)
# graph.add_arc(0, 4, 1)
# graph.add_arc(1, 0, 1)
# graph.add_arc(1, 2, 1)
# graph.add_arc(1, 3, 1)
# graph.add_arc(1, 4, 1)
# graph.add_arc(2, 0, 1)
# graph.add_arc(2, 1, 1)
# graph.add_arc(2, 3, 1)
# graph.add_arc(2, 4, 1)
# graph.add_arc(3, 0, 1)
# graph.add_arc(3, 1, 1)
# graph.add_arc(3, 2, 1)
# graph.add_arc(3, 4, 1)
# graph.add_arc(4, 0, 1)
# graph.add_arc(4, 1, 1)
# graph.add_arc(4, 2, 1)
# graph.add_arc(4, 3, 1)

all_cycles = dict() 
for start_mark in graph.get_all_marks():
    all_cycles[start_mark] = list( find_all_cycles(graph_repr=graph.adjacency_list_representation, start_mark=start_mark) )
pprint(all_cycles)

# pprint(len(graph.sh_arc_list()))
# print("----------------------------------------------------")
# pprint(graph.sh_accordance())
# print("----------------------------------------------------")
# pprint(graph.adjacency_list_representation)