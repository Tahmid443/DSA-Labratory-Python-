def knapsack_branch_bound(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)
    n = len(items)
    best = 0

    def bound(i, w, v):
        if w > capacity:
            return 0
        b = v
        for j in range(i, n):
            if w + items[j][0] <= capacity:
                w += items[j][0]
                b += items[j][1]
            else:
                b += (capacity - w) * items[j][1] / items[j][0]
                break
        return b

    def dfs(i, w, v):
        nonlocal best
        if w > capacity:
            return
        if i == n:
            best = max(best, v)
            return
        if bound(i, w, v) <= best:
            return
        # include
        dfs(i + 1, w + items[i][0], v + items[i][1])
        # exclude
        dfs(i + 1, w, v)

    dfs(0, 0, 0)
    return best


if __name__ == "__main__":
    print(knapsack_branch_bound([1, 3, 4, 5], [1, 4, 5, 7], 7))
