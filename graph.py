import pprint  # ***


class Graph:
    __arc_list: list[list[int, int, int]] = []
    __mark_name_accordance: dict[int, str] = {}


    def sh_accordance(self):                 # ***
        print(self.__mark_name_accordance)

    def sh_arc_list(self):                   # ***
        pprint.pprint(self.__arc_list)


    def __init__(self, arc_list: list[list[int, int, int]] = None):
        self.__arc_list = [] if arc_list is None else arc_list


    def adjacent_vertexes(self, v: int) -> list[int]:
        self._check_vertex(v)
        adj_verts = []
        v_outcoming_arcs = self._find_outcoming_arc_indexes(v)
        for out_arc_i in v_outcoming_arcs:
            adj_verts.append(self.__arc_list[out_arc_i][1])
        return adj_verts


    def first_adjacent(self, v: int) -> int:
        adj_verts = self.adjacent_vertexes(v)
        try:
            return adj_verts[0]
        except IndexError:
            raise Exception(f"Vertex {v} doesn't have adjacent vertexes")



    def next_adjacent(self, v: int, i: int) -> int:
        """Get mark of next adjacent vertex after adjacent vertex with mark i"""
        adj_verts = self.adjacent_vertexes(v)
        for ind in range(len(adj_verts)):
            if adj_verts[ind] == i:
                try:
                    return adj_verts[ind+1]
                except IndexError:
                    raise Exception(f"Vertex with mark {i} is the last adjacent vertex, there is no next")
        else:
            raise Exception(f"Vertex {v} doesn't have adjacent vertex with mark {i}")


    def ver_in_adjacent(self, v: int, i: int) -> int:
        """Get mark of vertex under index i from list of adjacent vertexes for v"""
        adj_verts = self.adjacent_vertexes(v)
        try:
            return adj_verts[i]
        except IndexError:
            raise Exception(f"There is no vertex under index {i} in the list of adjacent vertexes for vert {v}")



    def add_ver(self, name: str, v: int) -> None:
        self._check_no_vertex(v, name)
        self.__mark_name_accordance[v] = name
        self.__mark_name_accordance[name] = v


    def add_arc(self, v: int, w: int, weight: int) -> None:
        self._check_vertex(v, w)
        self.__arc_list.append( [v, w, weight] )


    def del_ver(self, name: str) -> None:
        self._check_vertex(name)
        v = self.__mark_name_accordance[name]
        self.del_all_arcs(v)
        del self.__mark_name_accordance[v]
        del self.__mark_name_accordance[name]

    
    def del_arc(self, v: int, w: int) -> None:
        """Delete first laid arc between v and w vertexes"""
        self._check_vertex(v, w)
        for arc_i in range(len(self.__arc_list)):
            if (self.__arc_list[arc_i][0] == v) and (self.__arc_list[arc_i][1] == w):
                del self.__arc_list[arc_i]
                break
        else:
            raise Exception(f"There is no arc between vertexes with marks {v} and {w}")


    def del_all_arcs(self, v: int) -> None:
        """Delete all arcs associated with vertex v"""
        self._check_vertex(v)
        all_arcs = sorted(self._find_outcoming_arc_indexes(v) + self._find_incoming_arc_indexes(v), reverse=True)
        for arc_i in all_arcs:
            del self.__arc_list[arc_i]

    
    def edit_ver_mark(self, name: str, new_v: int) -> None:
        """Change old mark for new one in arc list and accordance"""
        self._check_vertex(name)
        self._check_no_vertex(new_v)
        old_v = self.__mark_name_accordance[name]
        self.__mark_name_accordance[name] = new_v
        del self.__mark_name_accordance[old_v]
        self.__mark_name_accordance[new_v] = name
        for arc_i in range(len(self.__arc_list)):
            if self.__arc_list[arc_i][0] == old_v:
                self.__arc_list[arc_i][0] = new_v
            if self.__arc_list[arc_i][1] == old_v:
                self.__arc_list[arc_i][1] = new_v


    def edit_arc_weight(self, v: int, w: int, new_weight: int) -> None:
        self._check_vertex(v, w)
        for arc_i in range(len(self.__arc_list)):
            if (self.__arc_list[arc_i][0] == v) and (self.__arc_list[arc_i][1] == w):
                self.__arc_list[arc_i][2] = new_weight
                break
        else:
            raise Exception(f"There is no arc between vertexes with marks {v} and {w}")


    def _check_vertex(self, *mark_or_name: int | str) -> None:
        for vertex in mark_or_name:
            if self.__mark_name_accordance.get(vertex) == None:
                if isinstance(vertex, int):
                    raise Exception(f"Vertex with mark '{vertex}' doesn't exist!")
                elif isinstance(vertex, str):
                    raise Exception(f"Vertex with name '{vertex}' doesn't exist!")
                else:
                    raise Exception(f"Vertex '{vertex}' doesn't exist!")
                
    
    def _check_no_vertex(self, *mark_or_name: int | str) -> None:
        for vertex in mark_or_name:
            if self.__mark_name_accordance.get(vertex) != None:
                if isinstance(vertex, int):
                    raise Exception(f"Vertex with mark '{vertex}' already exists!")
                elif isinstance(vertex, str):
                    raise Exception(f"Vertex with name '{vertex}' already exists!")
                else:
                    raise Exception(f"Vertex '{vertex}' already exists!")


    def _find_outcoming_arc_indexes(self, v: int) -> list[int]:
        indexes = []
        for arc_i in range(len(self.__arc_list)):
            if self.__arc_list[arc_i][0] == v:
                indexes.append(arc_i)
        return indexes

    
    def _find_incoming_arc_indexes(self, v: int) -> list[int]:
        indexes = []
        for arc_i in range(len(self.__arc_list)):
            if self.__arc_list[arc_i][1] == v:
                indexes.append(arc_i)
        return indexes