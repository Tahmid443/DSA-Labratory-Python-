def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total = 0
    for weight, value in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)
            break
    return total


if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    print(fractional_knapsack(items, 50))
