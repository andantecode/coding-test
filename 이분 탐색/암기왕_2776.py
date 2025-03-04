# silver 4

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    number_of_note1 = int(input())
    note1 = set(map(int, input().split()))

    number_of_note2 = int(input())
    note2 = list(map(int, input().split()))

    for item in note2:
        if item in note1:
            print(1)
        else:
            print(0)

    
        

