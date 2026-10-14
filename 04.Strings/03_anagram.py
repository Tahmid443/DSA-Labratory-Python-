from collections import Counter


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def is_anagram_counter(s1, s2):
    return Counter(s1) == Counter(s2)


def is_anagram_array(s1, s2):
    if len(s1) != len(s2):
        return False
    count = [0] * 26
    for c in s1:
        count[ord(c) - ord("a")] += 1
    for c in s2:
        count[ord(c) - ord("a")] -= 1
        if count[ord(c) - ord("a")] < 0:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(is_anagram_counter("hello", "world"))
