S = [1, 1, 2, 2, 3, 4, 5, 6]
n = int(input())
ans = 0

S.sort(reverse=True)
chest = n
i = 0
while S:
    if chest < min(S):
        chest = n
        ans += 1
        i = 0
    else:
        if chest in S:
            S.remove(chest)
            chest = 0
        else:
            if chest >= S[i]:
                chest -= S[i]
                del S[i]
                i -= 1
    i += 1
if chest < n:
    ans += 1
print(ans)