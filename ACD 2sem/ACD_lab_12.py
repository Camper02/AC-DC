def get_prefix_func(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p


f = open('input.txt', 'r')
s = f.read()
t = input()
concat = t + '#' + s
pf = get_prefix_func(concat)
for i in range(len(t) + 1, len(t) + 1 + len(s)):
    if pf[i] == len(t):
        print(i - 2 * len(t))