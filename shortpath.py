def ts(case):
    if case == 0:
        file = 'dijkstraData.txt'
    if case == 1:
        file = 'dijkstratest1.txt'
    if case == 2:
        file = 'dijkstratest2.txt'
    if case == 3:
        file = 'dijkstratest3.txt'

    return(file)


def txt2graph(file):

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


def l(graph, v, w):
    return(graph[v][w])


def shortpath(graph, start):
    inf = 100000
    vted = set()
    min_dists = {}

    vted.add(start)
    min_dists[start] = 0

    while not vted == set(graph):

        best_edge = inf

        for v in vted:
            for w in set(graph[v]) - vted:
                if min_dists[v] + l(graph,v,w) < min_dists[v] + best_edge:
                    best_edge = l(graph,v,w)
                    v_star = v
                    w_star= w

        vted.add(w_star)
        min_dists[w_star] = min_dists[v_star] + best_edge

    return(min_dists)