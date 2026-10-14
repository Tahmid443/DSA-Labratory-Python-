def sqrt_floor(n):
    """Find floor(sqrt(n)) using binary search"""
    if n < 2:
        return n
    low, high = 1, n // 2
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


def min_capacity_to_ship(weights, days):
    """Ship packages within 'days' with minimum capacity"""

    def can_ship(cap):
        d, curr = 1, 0
        for w in weights:
            if curr + w > cap:
                d += 1
                curr = 0
            curr += w
        return d <= days

    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship(mid):
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    print(sqrt_floor(27))
    print(min_capacity_to_ship([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
