with open("input.txt", "r") as f:
    data = f.read()

sample = input()
l = len(sample)
state = 0

for i in range(len(data)):
    if data[i] == sample[state]:
        state += 1
    else:
        state = 0
        if data[i] == sample[state]:
            state += 1
    if state == l:
        state = 0
        print(i - l + 1)