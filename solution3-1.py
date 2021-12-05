import common

lines = common.get_lines(__file__)

N = len(lines[0])

count = [0] * N
for l in lines:
    for i, c in enumerate(l):
        if c == '1': count[i] += 1
print(count)

gamma = 0
for i in range(len(count)):
    gamma *= 2
    if count[i] >= len(lines) / 2:  gamma += 1
epsilon = (1 << N) - 1 - gamma

print("gamma and epsilon are {}, {}".format(gamma, epsilon))
print(gamma * epsilon)





            