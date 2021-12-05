import common

lines = common.get_lines(__file__)

count = 0
for i in range(len(lines) - 3):
    count += 1 if int(lines[i + 3]) > int(lines[i]) else 0

print(count)