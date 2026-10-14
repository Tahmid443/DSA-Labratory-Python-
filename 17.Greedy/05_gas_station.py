def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1


if __name__ == "__main__":
    print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
