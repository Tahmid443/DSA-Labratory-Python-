from collections import Counter


def min_window(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    left = 0
    best = (float("inf"), 0, 0)
    for right, c in enumerate(s):
        have[c] = have.get(c, 0) + 1
        if c in need and have[c] == need[c]:
            formed += 1
        while formed == required:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return "" if best[0] == float("inf") else s[best[1] : best[2] + 1]


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))
