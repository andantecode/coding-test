# silver 5

import sys

input = sys.stdin.readline

# 모음 하나 반드시 포함
# 모음이 3개 연속, 자음이 3개 연속오면 안 됨
# 같은 글자가 연속적으로 두 번 오면 안되지만, ee, oo는 예외

def is_vowel(char):
    if char in ["a", "e", "i", "o", "u"]:
        return True
    return False

def is_acceptable(target):
    target = list(target)
    ans = [False, True, True]

    # 모음 하나 반드시 포함
    for t in target:
        if is_vowel(t):
            ans[0] = True
            break
    
    # 모음이 3개 연속, 자음이 3개 연속오면 안 됨
    count = 1
    switch = True
    for i, t in enumerate(target):
        if i == 0:
            switch = is_vowel(t)
        else:
            now = is_vowel(t)
            if switch == now:
                count += 1
            else:
                count = 1

            switch = now

        if count >= 3:
            ans[1] = False

    # 같은 글자가 2번 연속으로 오면 안되지만, ee, oo는 가능
    previous = ""
    for i, t in enumerate(target):
        if i == 0:
            previous = t
        else:
            if previous == t and t not in ["e", "o"]:
                ans[2] = False
                break
            previous = t

    if sum(ans) == 3:
        return True
    return False

while True:
    target = input().strip()

    if target == "end":
        break

    if is_acceptable(target):
        print(f"<{target}> is acceptable.")
    else:
        print(f"<{target}> is not acceptable.")
    