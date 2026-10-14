import sys


def solve():
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))


if __name__ == "__main__":
    solve()
