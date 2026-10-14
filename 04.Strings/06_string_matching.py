def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    results = []
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            results.append(i)
    return results


if __name__ == "__main__":
    print(naive_search("AABAACAADAABAABA", "AABA"))
