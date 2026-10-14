def is_palindrome(s):
    return s == s[::-1]


def is_palindrome_two_pointer(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_alpha(s):
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]


if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome_two_pointer("racecar"))
    print(is_palindrome_alpha("A man, a plan, a canal: Panama"))
