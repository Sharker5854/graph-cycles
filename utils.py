def trans_matrix_to_list(matrix: list[list[int]]) -> list[list[int, int, int]]:
    is_matrix_square(matrix)
    res_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                res_list.append([i, j, matrix[i][j]])
    return res_list


def is_matrix_square(matrix: list[list[int]]) -> None:
    for string in matrix:
        if not(len(string) == len(matrix)):
            raise Exception("The matrix is not square")
        

def find_all_cycles(graph_repr: dict[int, dict[int, int]], start_mark: int, cur_mark: int = None, cur_length: int = 0, route: list = []):
    # print(f"{cur_mark=}")
    # print(f"{route=}")
    if len(route) == 0:
        cur_mark = start_mark
        route.append(start_mark)
    if cur_mark == start_mark and cur_length > 0:  # выходим, если прошли цикл и пришли в начальный узел
        print((route, cur_length))
        return (route, cur_length)
    else:
        keys = list(graph_repr[cur_mark].keys())
        if route != [start_mark]:
            for next_mark_ind in range(len(keys)-1, -1, -1):                  # удаляем из последующих возможных узлов те, которые уже были пройдены
                if (keys[next_mark_ind] in route[1:]):                        # после первого хопа - среди возможных путей оставляем start_mark
                    del keys[next_mark_ind]
        print(keys)
        for mark in keys:
            return find_all_cycles(
                graph_repr=graph_repr, 
                start_mark=start_mark, 
                cur_mark=mark, 
                cur_length=cur_length+graph_repr[cur_mark][mark], 
                route=route+[mark]
            )