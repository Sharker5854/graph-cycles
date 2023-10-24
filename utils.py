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
        

def find_all_cycles(graph_repr: dict[int, dict[int, int]], start_mark: int, route: list[int], cur_mark: int = None, cur_length: int = 0):
    """Делаем рекурсивный обход в глубину и находим все возможные циклы, которые начинаются в узле start_mark и 
    заканчиваются в нём же, а также их длину, которая равна сумме весов дуг повстречавшихся на пути"""
    if len(route) == 1:            # если только начинаем обход со стартового узла, то
        cur_mark = start_mark      # задаем значение текущего узла равное стартовому
    if cur_mark == start_mark and cur_length > 0:  # возвращаем значение, если прошли цикл и пришли в начальный узел
        yield (route, cur_length)  # возвращаемый формат: ( [<маршрут_цикла>], длина_цикла )
    else:
        keys = list(graph_repr[cur_mark].keys())   # формируем массив из маркировок всех смежных узлов
        if route != [start_mark]:  # если сейчас не самый первый переход из стартового узла, то
            for next_mark_ind in range(len(keys)-1, -1, -1):      # удаляем из смежных узлов те, которые уже были пройдены (чтобы не происходило бесконечного зацикливания)
                if (keys[next_mark_ind] in route[1:]):            # после первого перехода всегда оставляем start_mark среди смежных узлов, чтобы цикл было возможно замкнуть
                    del keys[next_mark_ind]
        for mark in keys:                   # для всех доступных смежных узлов
            yield from find_all_cycles(     # продолжаем углубляться
                graph_repr=graph_repr, 
                start_mark=start_mark, 
                cur_mark=mark, 
                cur_length=cur_length+graph_repr[cur_mark][mark], 
                route=route+[mark]
            )