# silver 4

import sys
from collections import Counter

input = sys.stdin.readline

# 랭킹 리스트에 올라갈 수 있는 점수의 개수 P
# 리스트에 있는 점수 N개

N, target, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
    counter = Counter(scores)
    counter.update([target])

    count = 0
    for key in sorted(counter.keys(), reverse=True):
        rank = count + 1
        count += counter[key]

        if key == target:
            # print(count)
            if count <= P:
                print(rank)
            else:
                print(-1)

            break

else:
    if P != 0:
        print(1)


        
        
