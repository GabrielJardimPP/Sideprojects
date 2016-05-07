'''Implementation of Dijkstra's algorithm
By Gabriel Jardim Pereira Pinto

O(n^2) solution of Coursera's Algorithms course , programming question 5'''


def txt2graph(file):  # opens file converting to graph in dictionary structure

    fil = open(file, 'r')
    graph = {}

    for line in fil:
        data = line.split()
        v = int(data[0])

        for f_node in range(1, len(data)):

            edg_inf = data[f_node].split(',')
            w, weight = [int(edg_inf[i]) for i in range(len(edg_inf))]

            try:
                graph[v][w] = weight

            except KeyError:
                graph[v] = {}
                graph[v][w] = weight

    return(graph)


def shortpath(graph, start):  # Find shortest path from start to all others
    inf = 100000
    vted = set()
    min_dists = {}

    vted.add(start)
    min_dists[start] = 0

    while not vted == set(graph):

        best_dist = inf

        for start in vted:
            for neighbour in graph[start]:
                if neighbour not in vted:
                    current_dist = graph[start][neighbour] + min_dists[start]

                    if current_dist < best_dist:
                        best_neighbour = neighbour
                        best_dist = current_dist

        vted.add(best_neighbour)
        min_dists[best_neighbour] = best_dist

    return(min_dists)


def answer(graph, start):  # Uses question information to return answer

    min_dists = shortpath(graph, start)
    desired = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

    answers = []
    for node in desired:
        answers.append(min_dists[node])

    return(answers)
