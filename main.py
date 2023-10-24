from graph import Graph
from utils import trans_matrix_to_list, find_all_cycles


arc_matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 3, 0, 3, 0, 3, 0, 0]
]
graph1 = Graph(arc_list=trans_matrix_to_list(arc_matrix))   # в конструктор Graph'a передаём готовый список дуг, который получили из матрицы весов дуг
x = int(input("Cycle length: "))  # 9 (total 21),   13 (total 40)

all_cycles = dict()
for start_mark in graph1.get_all_marks():
    all_cycles[start_mark] = list( find_all_cycles(graph_repr=graph1.adjacency_list_representation, start_mark=start_mark, route=[start_mark]) )

total = 0
for start_mark, cycles in all_cycles.items():
    cycles_with_length_x = list(filter(lambda cycl: cycl[1] == x, cycles))
    total += len(cycles_with_length_x)
    print(f"For start vertex with mark '{start_mark}' was found {len(cycles_with_length_x)} cycles with length {x}.")
    for cycl in cycles_with_length_x:
        print(" -> ".join(list(map(str, cycl[0]))))
    print("\n" + "-"*30 + "\n")

print(f"TOTAL: {total} cycles.", end="\n\n")










graph2 = Graph()

graph2.add_ver("A", 0)
graph2.add_ver("B", 1)
graph2.add_ver("C", 2)
graph2.add_ver("D", 3)
graph2.add_ver("E", 4)

graph2.add_arc(0, 1, 1)
graph2.add_arc(0, 2, 1)
graph2.add_arc(0, 3, 1)
graph2.add_arc(0, 4, 1)
graph2.add_arc(1, 0, 1)
graph2.add_arc(1, 2, 1)
graph2.add_arc(1, 3, 1)
graph2.add_arc(1, 4, 1)
graph2.add_arc(2, 0, 1)
graph2.add_arc(2, 1, 1)
graph2.add_arc(2, 3, 1)
graph2.add_arc(2, 4, 1)
graph2.add_arc(3, 0, 1)
graph2.add_arc(3, 1, 1)
graph2.add_arc(3, 2, 1)
graph2.add_arc(3, 4, 1)
graph2.add_arc(4, 0, 1)
graph2.add_arc(4, 1, 1)
graph2.add_arc(4, 2, 1)
graph2.add_arc(4, 3, 1)

x = int(input("Cycle length: "))   # 2 (total 20), 3 (total 60)

all_cycles = dict()
for start_mark in graph2.get_all_marks():
    all_cycles[start_mark] = list( find_all_cycles(graph_repr=graph2.adjacency_list_representation, start_mark=start_mark, route=[start_mark]) )

total = 0
for start_mark, cycles in all_cycles.items():
    cycles_with_length_x = list(filter(lambda cycl: cycl[1] == x, cycles))
    total += len(cycles_with_length_x)
    print(f"For start vertex with mark '{start_mark}' was found {len(cycles_with_length_x)} cycles with length {x}.")
    for cycl in cycles_with_length_x:
        print(" -> ".join(list(map(str, cycl[0]))))
    print("\n" + "-"*30 + "\n")

print(f"TOTAL: {total} cycles.", end="\n\n")