
from collections import deque

def bfs_8_puzzle(start, goal):
    start = tuple(start)
    goal = tuple(goal)

    queue = deque([start])
    parent = {start: None}
    action_taken = {start: None}

    moves = {
        "Up": -3,
        "Down": 3,
        "Left": -1,
        "Right": 1
    }

    while queue:
        state = queue.popleft()

        if state == goal:
            path = []
            while parent[state] is not None:
                path.append((action_taken[state], state))
                state = parent[state]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for action, change in moves.items():
            if action == "Up" and row == 0:
                continue
            if action == "Down" and row == 2:
                continue
            if action == "Left" and col == 0:
                continue
            if action == "Right" and col == 2:
                continue

            new_zero = zero + change
            new_state = list(state)

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            new_state = tuple(new_state)

            if new_state not in parent:
                parent[new_state] = state
                action_taken[new_state] = action
                queue.append(new_state)

    return None


start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = bfs_8_puzzle(start, goal)

print("========== 8 Puzzle using BFS ==========")

if solution is not None:
    print("Solution found!")
    print("Number of moves:", len(solution))

    for i, (action, state) in enumerate(solution, 1):
        print("\nMove", i, ":", action)
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
else:
    print("No solution found.")
