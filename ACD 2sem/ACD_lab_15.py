def color_graph(graph, colors):
    colored_nodes = {}
    for node in graph:
        used_colors = set(colored_nodes.get(neighbour) for neighbour in graph[node] if neighbour in colored_nodes)
        available_colors = [color for color in colors if color not in used_colors]
        colored_nodes[node] = available_colors[0]
    return colored_nodes

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Blue', 'Green']

colored_nodes = color_graph(graph, colors)
print(colored_nodes)