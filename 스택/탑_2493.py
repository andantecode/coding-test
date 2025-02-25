import sys

input = sys.stdin.readline
N = int(input())
towers = list(map(int, input().split()))
stack = []
ans = [0] * N

for i in range(N - 1, -1, -1):
    # 스택에서 꺼낸 타워가 현재 타워보다 작거나 같을 때까지 반복 (3이랑 4를 꺼냈고, 현재 타워 높이는 5일 때, 3과 4에서 쏜 신호는 현재 타워에서 수신)
    while stack and towers[stack[-1]] <= towers[i]:
        ans[stack.pop()] = i + 1
    stack.append(i)

print(" ".join(map(str, ans)))
