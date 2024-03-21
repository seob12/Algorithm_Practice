import heapq
import sys

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def path(self):
        if self.parent is None:
            return [self.state]
        return self.parent.path() + [self.state]

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def move_up(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 1, 2]:
        new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
        return new_state
    return None

def move_down(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]:
        new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
        return new_state
    return None

def move_left(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:
        new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
        return new_state
    return None

def move_right(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:
        new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
        return new_state
    return None

def expand(node):
    expanded_nodes = []
    expanded_nodes.append(Node(move_up(node.state), parent=node, action="Up", cost=node.cost + 1, heuristic=calculate_heuristic(move_up(node.state))))
    expanded_nodes.append(Node(move_down(node.state), parent=node, action="Down", cost=node.cost + 1, heuristic=calculate_heuristic(move_down(node.state))))
    expanded_nodes.append(Node(move_left(node.state), parent=node, action="Left", cost=node.cost + 1, heuristic=calculate_heuristic(move_left(node.state))))
    expanded_nodes.append(Node(move_right(node.state), parent=node, action="Right", cost=node.cost + 1, heuristic=calculate_heuristic(move_right(node.state))))
    expanded_nodes = [node for node in expanded_nodes if node.state is not None]
    return expanded_nodes

def calculate_heuristic(state):
    heuristic = 0
    for i in range(len(state)):
        if state[i] != 0 and state[i] != i + 1:
            heuristic += 1
    return heuristic

def branch_and_bound(initial_state, goal_state):
    visited = set()
    heap = []
    heapq.heappush(heap, Node(initial_state, cost=0, heuristic=calculate_heuristic(initial_state)))
    while heap:
        node = heapq.heappop(heap)
        if node.state == goal_state:
            return node.path()
        visited.add(tuple(node.state))
        expanded_nodes = expand(node)
        for expanded_node in expanded_nodes:
            if tuple(expanded_node.state) not in visited:
                heapq.heappush(heap, expanded_node)
    return None

# 테스트 코드
initial_state = [1, 2, 3, 0, 4, 6, 7, 5, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

solution = branch_and_bound(initial_state, goal_state)
if solution is not None:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
