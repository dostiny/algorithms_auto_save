import sys

input = sys.stdin.readline

def solve(n: int) -> str:
    return 'long ' * (n // 4) + 'int'

n = int(input())

print(solve(n))