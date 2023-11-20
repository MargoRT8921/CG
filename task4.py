# the shortest path
from collections import defaultdict
import heapq

def shortest_path(graph, start, end):
    # Создаем словарь для хранения кратчайшего пути от стартовой вершины до каждой другой вершины
    shortest_paths = defaultdict(list)
    # Инициализируем очередь с приоритетами
    queue = [(0, start)]
    # Устанавливаем расстояние до стартовой вершины равным 0
    shortest_paths[start] = [0, [start]]

    while queue:
        # Извлекаем вершину с наименьшим расстоянием
        (dist, current_vertex) = heapq.heappop(queue)

        # Проверяем, достигли ли мы конечной вершины
        if current_vertex == end:
            return shortest_paths[end]

        # Просматриваем соседние вершины текущей вершины
        for neighbor, weight in graph[current_vertex]:
            # Вычисляем новое расстояние от стартовой вершины до соседней вершины
            distance = dist + weight
            # Если новое расстояние меньше текущего расстояния
            if distance < shortest_paths[neighbor][0]:
                # Обновляем кратчайший путь до соседней вершины
                shortest_paths[neighbor] = [distance, shortest_paths[current_vertex][1] + [neighbor]]
                # Добавляем соседнюю вершину в очередь с приоритетами для дальнейшего обхода
                heapq.heappush(queue, (distance, neighbor))

    # Если не удалось найти путь
    return "Путь не найден"

# Пример использования алгоритма
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': [('E', 2)],
    'E': []
}

start_vertex = 'A'
end_vertex = 'E'

result = shortest_path(graph, start_vertex, end_vertex)
print(f"Кратчайший путь от {start_vertex} до {end_vertex}: {result[1]}")
print(f"Расстояние: {result[0]}")
