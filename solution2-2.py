import common

lines = common.get_lines(__file__)

h, d, a = 0, 0, 0
for l in lines:
    action, num = l.split()
    if action == 'forward':
        h += int(num)
        d += int(num) * a
    elif action == 'down':
        a += int(num)
    elif action == 'up':
        a -= int(num)
    else:
        raise ValueError('instruction is not supported')

print(h * d)