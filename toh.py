
def hanoi_state_space(n):
    pegs = [list(range(n, 0, -1)), [], []]
    names = ["Source", "Auxiliary", "Destination"]
    moves = []

    def move_disk(src, dst):
        disk = pegs[src].pop()
        pegs[dst].append(disk)
        moves.append(
            f"Move disk {disk} from {names[src]} to {names[dst]}"
        )

    def solve(k, src, aux, dst):
        if k == 0:
            return

        solve(k - 1, src, dst, aux)
        move_disk(src, dst)
        solve(k - 1, aux, src, dst)

    print("Initial State:", pegs)
    solve(n, 0, 1, 2)

    print("\nSolution Path:")
    for i, move in enumerate(moves, 1):
        print(f"{i}. {move}")

    print("\nGoal State:", pegs)
    print("Total Moves:", len(moves))


n = int(input("Enter number of disks: "))
hanoi_state_space(n)
