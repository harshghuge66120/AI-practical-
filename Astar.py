
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(
        abs(i//3 - GOAL.index(x)//3) +
        abs(i%3 - GOAL.index(x)%3)
        for i, x in enumerate(s) if x != 0
    )

def astar(start):
    pq = [(h(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)
        if s in visited:
            continue
        visited.add(s)
        path = path + [s]

        if s == GOAL:
            return path

        z = s.index(0)
        for d in [-3, 3, -1, 1]:
            nz = z + d
            if 0 <= nz < 9 and not (
                (d == -1 and z % 3 == 0) or
                (d == 1 and z % 3 == 2)
            ):
                t = list(s)
                t[z], t[nz] = t[nz], t[z]
                t = tuple(t)

                if t not in visited:
                    heapq.heappush(
                        pq, (g+1+h(t), g+1, t, path)
                    )
    return None

start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))
solution = astar(start)

if solution:
    print("Moves:", len(solution)-1)
    for s in solution:
        print(s[:3], s[3:6], s[6:])
else:
    print("No solution found")
