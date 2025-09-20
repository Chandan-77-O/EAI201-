import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq



edges = [
    ("Main Gate", "ID Gate", 170),
    ("ID Gate", "Library", 70),
    ("Library", "Lawn Area", 100),
    ("Library", "Vendi", 30),         
    ("Lawn Area", "ACB2", 60),
    ("ACB2", "Food court", 200),
    ("Food court", "Hostel", 150),
    ("Hostel", "Sports", 450),
    ("Lawn Area", "Vendi", 65),
    ("Vendi", "1Floor", 20),
    ("1Floor", "Cafe", 20),
]

# Build adjacency list with weights
graph = {}
for u, v, w in edges:
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))  # Undirected graph


def bfs(start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

def ucs(start, goal):
    pq = [(0, [start])]  # (cost, path)
    visited = set()

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(pq, (cost + weight, new_path))
    return None, float('inf')



def draw_graph():
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = {
        "Main Gate": (0, 0),
        "ID Gate": (0, 1),
        "Library": (1, 2),
        "Lawn Area": (0, 2),
        "Vendi": (-1, 2),
        "1Floor": (-2, 2),
        "Cafe": (-3, 2),
        "ACB2": (0, 3),
        "Food court": (0, 4),
        "Hostel": (1, 4),
        "Sports": (1, 5)
    }

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=3000, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=9, font_color='black')

    plt.title("Campus Map (Main Stairs removed, Library ↔ Vendi: 30m)", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def print_path(path, cost=None):
    if not path:
        print("No path found.")
    else:
        print("Path:")
        print(" -> ".join(path))
        if cost is not None:
            print(f"Total Distance: {cost} meters")

def main():
    print("Campus Pathfinding (Main Stairs removed)")
    print("\nAvailable Locations:")
    for location in graph:
        print("-", location)

    start = input("\nEnter START location: ").strip()
    goal = input("Enter GOAL location: ").strip()

    if start not in graph or goal not in graph:
        print("Invalid location(s).")
        return

    print("\nChoose algorithm:")
    print("1. BFS")
    print("2. DFS")
    print("3. UCS")
    choice = input("Enter choice (1/2/3): ").strip()

    print("\nFinding path...\n")

    if choice == "1":
        path = bfs(start, goal)
        print("BFS Result:")
        print_path(path)
    elif choice == "2":
        path = dfs(start, goal)
        print("DFS Result:")
        print_path(path)
    elif choice == "3":
        path, cost = ucs(start, goal)
        print("UCS Result:")
        print_path(path, cost)
    else:
        print("Invalid choice.")

    # Visualize the graph
    draw_graph()

if __name__ == "__main__":
    main()
