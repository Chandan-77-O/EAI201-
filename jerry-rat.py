from collections import deque
import heapq

graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("A", 2), ("D", 3), ("E", 5)],
    "C": [("A", 4), ("F", 2), ("G", 6)],
    "D": [("B", 3), ("H", 4)],
    "E": [("B", 5), ("H", 2), ("I", 3)],
    "F": [("C", 2), ("I", 4)],
    "G": [("C", 6), ("J", 5)],
    "H": [("D", 4), ("E", 2), ("K", 7)],
    "I": [("E", 3), ("F", 4), ("K", 1)],
    "J": [("G", 5), ("K", 2)],
    "K": [("H", 7), ("I", 1), ("J", 2), ("L", 6)],
    "L": [("K", 6)]
}

print("Graph (12 nodes):")
for node, edges in graph.items():
    print(node, "->", edges)
print("-" * 40)


def dfs(start, goal):
    stack = [(start, [start], 0)]
    visited = set()
    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            print("Path:", path, "Cost:", cost)
            return

        if node not in visited:
            visited.add(node)
            for neigh, c in graph[node]:
                if neigh not in visited:
                    stack.append((neigh, path + [neigh], cost + c))

    print("No path")


def bfs(start, goal):
    queue = deque([(start, [start], 0)])
    visited = set()
    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            print("Path:", path, "Cost:", cost)
            return

        if node not in visited:
            visited.add(node)
            for neigh, c in graph[node]:
                if neigh not in visited:
                    queue.append((neigh, path + [neigh], cost + c))

    print("No path")


def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path, "Cost:", cost)
            return

        if node not in visited:
            visited.add(node)
            for neigh, c in graph[node]:
                if neigh not in visited:
                    heapq.heappush(pq, (cost + c, neigh, path + [neigh]))

    print("No path")


start = input("Enter starting node of rat: ").upper()
goal = input("Enter where the cheese is : ").upper()
algo = input("Choose algorithm (1.DFS /2.BFS /3.UCS): ")

if algo == "1":
    dfs(start, goal)
elif algo == "2":
    bfs(start, goal)
elif algo == "3":
    ucs(start, goal)
else:
    print("Invalid choice")
