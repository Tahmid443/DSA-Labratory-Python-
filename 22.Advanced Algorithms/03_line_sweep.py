def max_overlapping_intervals(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))
    events.sort()
    curr = best = 0
    for _, delta in events:
        curr += delta
        best = max(best, curr)
    return best


if __name__ == "__main__":
    print(max_overlapping_intervals([(1, 4), (2, 5), (3, 6), (5, 7)]))
