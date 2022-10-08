ansList = []
List = [[] for _ in range(1001)]


def dfs(start, end, routes, total, x, y, visited, List):
    if start == end:
        if visited[x-1] and visited[y-1]:
            if routes.index(x) < routes.index(y):
                ansList.append(total)

                return

    else:

        routes.append(start)
        visited[start-1] = True
        for next in List[start]:
            nx, nw = next
            if visited[nx-1]:
                continue
            else:
                dfs(nx, end, routes, total + nw, x, y, visited, List)
                visited[nx-1] = False


def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    visited = [False] * g_edges
    routes = []
    for s, e, w in zip(g_from, g_to, g_weight):
        List[s].append((e, w))
        List[e].append((s, w))
    dfs(1, g_edges, routes, 0, x, y, visited, List)
    return ansList

print(minCostPath(4,[1, 1, 2, 2, 3],[2, 4, 4, 3, 4],[6, 9, 10, 6, 11]
                  ,2,3))