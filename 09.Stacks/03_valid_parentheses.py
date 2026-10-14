def is_valid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


if __name__ == "__main__":
    print(is_valid("()[]{}"))
    print(is_valid("([)]"))
