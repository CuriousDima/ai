from collections import defaultdict, deque
from typing import List, Set


# "0000" -> ['9000', '0900', '0090', '0009', '1000', '0100', '0010', '0001']
# "1234" -> ['0234', '1134', '1224', '1233', '2234', '1334', '1244', '1235']
def get_neighbors(node: str) -> List[str]:
    return [
        node[:i] + str((int(node[i]) + d) % 10) + node[i + 1 :]
        for d in (-1, 1)
        for i in range(4)
    ]


# While I build graph for with all possible states, it is not necessary
# for memory-efficient solution.
def build_graph(deadends: Set[int]) -> defaultdict[str, Set[str]]:
    graph = defaultdict(set)
    for i in range(10000):
        state = "{:04d}".format(i)
        # Deadend nodes have no neighbors.
        # They are like an island in the graph.
        if state in deadends:
            continue
        for neighbor in get_neighbors(state):
            if neighbor not in deadends:
                # Since we loop over all possible states,
                # we don't need to explicitly set back edges.
                graph[state].add(neighbor)
    return graph


def solve(g, goal):
    # If the goal is a deadend, we can't reach it.
    if len(g[goal]) == 0:
        return -1

    q = deque([("0000", 0)])
    # `frontier` is not necessary for memory-efficient solution.
    # `and neighbor not in frontier` just help to limit the search space.
    frontier = set(["0000"])
    visited = set()
    while q:
        node, depth = q.popleft()
        frontier.remove(node)
        visited.add(node)
        if node == goal:
            return depth
        # If we want to build memory-efficient solution, and avoid
        # spending time on building graph, we can use modified get_neighbors here.
        for neighbor in g[node]:
            if neighbor not in visited and neighbor not in frontier:
                q.append((neighbor, depth + 1))
                frontier.add(neighbor)
    return -1


if __name__ == "__main__":
    deadends = set(["0201", "0101", "0102", "1212", "2002"])
    g = build_graph(deadends)
    assert solve(g, "0202") == 6

    deadends = ["8888"]
    g = build_graph(deadends)
    assert solve(g, "0009") == 1

    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    g = build_graph(deadends)
    assert solve(g, "8888") == -1
