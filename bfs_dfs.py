root = {
    'a': ['b', 'c'],
    'b': ['e'],
    'c': ['d', 'f'],
    'e': ['g'],


}
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


def depth_first_search_while(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


def breath_first_search_while(graph, source):
    queue = [source]

    while len(queue) > 0:
        queue.reverse()
        current = queue.pop()
        queue.reverse()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


def depth_first_search_recursive(graph, source):
    if not (source in graph):
        return
    print(source)
    # LOOP
    for neighbor in graph[source]:
        depth_first_search_recursive(graph, neighbor)


# depth_first_search_recursive(root, 'a')
#breath_first_search_while(graph,'a')
depth_first_search_while(graph,'a')