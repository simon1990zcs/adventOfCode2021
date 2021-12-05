import common

lines = common.get_lines(__file__)

x, y = 0, 0
for l in lines:
    action, num = l.split()
    if action == 'forward':
        x += int(num)
    elif action == 'down':
        y += int(num)
    elif action == 'up':
        y -= int(num)
    else:
        raise ValueError('instruction is not supported')

print(x * y)