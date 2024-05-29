def forming_d(pattern):
    d = [len(pattern) for i in range(256)]
    new_p = pattern[::-1]
    for i in range(1, len(new_p)):
        d[ord(new_p[i])] = i

    return d


def search(string, pattern):
    d = forming_d(pattern)
    x = 2
    len_p = j = k = len(pattern)
    counter = 0
    l = len(string)
    while x <= l and j > 0:
        if pattern[j - 1] == string[k - 1]:
            j -= 1
            k -= 1
        else:

            if string[k - 1] == "c" and x > k - 1:
                x = k - 1
            else:
                counter = x - 2
                x += d[ord(string[k - 1])]
                k = x
                j = len_p

        print(x, j, k)
    if j <= 0:
        return counter
    else:
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