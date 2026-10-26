
def goal_stack_planning():
    state = {
        "OnTable(A)", "OnTable(B)", "OnTable(C)",
        "Clear(A)", "Clear(B)", "Clear(C)", "HandEmpty"
    }

    goals = ["On(A,B)", "On(B,C)"]
    actions = []

    # Achieve On(A,B)
    if "On(A,B)" not in state:
        actions.append("PickUp(A)")
        state.remove("OnTable(A)")
        state.remove("Clear(A)")
        state.remove("HandEmpty")
        state.add("Holding(A)")

        actions.append("Stack(A,B)")
        state.remove("Holding(A)")
        state.remove("Clear(B)")
        state.add("On(A,B)")
        state.add("Clear(A)")
        state.add("HandEmpty")

    # Achieve On(B,C)
    if "On(B,C)" not in state:
        actions.append("UnStack(A,B)")
        state.remove("On(A,B)")
        state.remove("Clear(A)")
        state.remove("HandEmpty")
        state.add("Holding(A)")
        state.add("Clear(B)")

        actions.append("PutDown(A)")
        state.remove("Holding(A)")
        state.add("OnTable(A)")
        state.add("Clear(A)")
        state.add("HandEmpty")

        actions.append("PickUp(B)")
        state.remove("OnTable(B)")
        state.remove("Clear(B)")
        state.remove("HandEmpty")
        state.add("Holding(B)")

        actions.append("Stack(B,C)")
        state.remove("Holding(B)")
        state.remove("Clear(C)")
        state.add("On(B,C)")
        state.add("Clear(B)")
        state.add("HandEmpty")

    print("========== Goal Stack Planning ==========")

    print("\nInitial State:")
    print("{OnTable(A), OnTable(B), OnTable(C), Clear(A), Clear(B), Clear(C), HandEmpty}")

    print("\nGoal State:")
    print("{On(A,B), On(B,C), OnTable(C), Clear(A), HandEmpty}")

    print("\nPlan Generated:")
    for i, action in enumerate(actions, 1):
        print(f"Step {i}: {action}")


goal_stack_planning()
