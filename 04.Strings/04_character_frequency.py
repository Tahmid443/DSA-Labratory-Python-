from collections import Counter


def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq


def char_frequency_counter(s):
    return dict(Counter(s))


if __name__ == "__main__":
    print(char_frequency("hello"))
    print(char_frequency_counter("programming"))
