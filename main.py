from graph import Graph


graph = Graph()

graph.add_ver("A", 0)
graph.add_ver("B", 1)
graph.add_ver("C", 2)
graph.add_ver("D", 3)
graph.add_ver("E", 4)
graph.add_ver("F", 5)
graph.add_ver("G", 6)

graph.add_arc(2, 0, 13)
graph.add_arc(4, 5, 10)
graph.add_arc(3, 2, 21)
graph.add_arc(2, 3, 18)
graph.add_arc(4, 0, 543)
graph.add_arc(2, 4, 669)
graph.add_arc(5, 2, 25)
graph.add_arc(1, 2, 14)
graph.add_arc(0, 6, 144)

graph.edit_ver_mark("C", 100)
graph.edit_arc_weight(100, 3, 19)

print(graph.first_adjacent(4))
print(graph.next_adjacent(100, 3))
print(graph.ver_in_adjacent(100, 1))
graph.sh_arc_list()
graph.sh_accordance()