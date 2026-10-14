def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    result = [activities[0]]
    last_end = activities[0][1]
    for start, end in activities[1:]:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    return result


if __name__ == "__main__":
    acts = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 9),
        (5, 9),
        (6, 10),
        (8, 11),
        (8, 12),
        (2, 14),
        (12, 16),
    ]
    print(activity_selection(acts))
