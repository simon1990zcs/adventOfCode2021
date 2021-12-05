import common

lines = common.get_lines(__file__)
N = len(lines[0])

def get_last_line_number(lines, common):
    for i in range(N):

        def get_most_common_char():
            count = 0
            for l in lines:
                if l[i] == '1': count += 1
            return '1' if count >= len(lines) / 2 else '0'

        c = get_most_common_char()
        lines = [l for l in lines if (common and l[i] == c) or (not common and l[i] != c)]
        if len(lines) == 1:  
            return int(lines[0], 2)


oxy = get_last_line_number(lines, True)
co2 = get_last_line_number(lines, False)

print(f'oxy is {oxy}, co2 is {co2}, the result is {oxy * co2}')


