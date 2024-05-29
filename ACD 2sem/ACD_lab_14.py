def search(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:m])

    for i in range(n - m + 1):
        if pattern_hash == text_hash and pattern == text[i:i + m]:
            return i
        if i < n - m:
            text_hash = hash(text[i + 1:i + m + 1])

    return -1


with open("input.txt", "r") as f:
    data = f.read()

sample = input()

s = search(data, sample)

c = 0
while s != -1:
    print(s + c)
    c += s + 3
    s = search(data[c::], sample)