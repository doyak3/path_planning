import matplotlib.pyplot as plt
from bfs import *
from plot_me import *

# Define the user's specified building graph
building_graph = {
    'R1': ['R2'],
    'R2': ['R1', 'R3'],
    'R3': ['R2', 'R4'],
    'R4': ['R3', 'R5', 'R7'],
    'R5': ['R4', 'R6'],
    'R6': ['R5'],
    'R7': ['R4', 'R8'],
    'R8': ['R7', 'R9'],
    'R9': ['R8', 'R10'],
    'R10': ['R9', 'R11'],
    'R11': ['R10']
}


# Use the function to generate the undirected graph
graph = building_graph#make_undirected_graph(building_graph)

# Get user input for start and goal nodes
start_node = input("Enter the start node (e.g., R1): ").strip()
goal_node = input("Enter the goal node (e.g., R11): ").strip()

# Find the shortest path
shortest_path = bfs_recursive(graph, start_node, goal_node)

if shortest_path is None:
    print(f"No path found from {start_node} to {goal_node}.")
else:
    print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")
    # Plot the building layout with the path highlighted
    plot_building_layout(graph, positions, shortest_path)
