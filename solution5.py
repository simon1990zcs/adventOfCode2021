import common
import re

lines = common.get_lines(__file__)
N = 1000

table = [[0] * 1000 for _ in range(N)]
coordinates = []
for l in lines:
    sl = re.findall('\d+', l)
    coordinates.append([int(_) for _ in sl])

def count_table():
    # count points >= 2
    return sum(sum(1 for _ in row if _ >= 2) for row in table)

def part_one():
    # mark count
    for x1, y1, x2, y2 in coordinates:
        if x1 == x2:
            sy, ly = min(y1, y2), max(y1, y2)
            for ty in range(sy, ly + 1):
                table[x1][ty] += 1
        elif y1 == y2:
            sx, lx = min(x1, x2), max(x1, x2)
            for tx in range(sx, lx + 1):
                table[tx][y1] += 1
        
    return count_table()
    

def part_two():
    # mark count
    for x1, y1, x2, y2 in coordinates:
        dx = 0 if x2 == x1 else (x2 - x1) // abs(x2 - x1)
        dy = 0 if y2 == y1 else (y2 - y1) // abs(y2 - y1)
        r = max(abs(x1 - x2), abs(y1 - y2))
        for n in range(r + 1):
            table[x1 + dx * n][y1 + dy * n] += 1
    
    return count_table()
