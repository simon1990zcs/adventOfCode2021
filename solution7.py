import common

lines = common.get_lines(__file__)
numbers = [int(_) for _ in lines[0].split(',')]

def part_one():
    numbers.sort()
    p = numbers[len(numbers) // 2]
    return sum(abs(n - p) for n in numbers)


def part_two():

    def fuel(x, y):
        dis = abs(y - x)
        return dis * (dis + 1) // 2
    
    def fuel_sum(p):
        return sum(fuel(n, p) for n in numbers)

    average = sum(numbers) / len(numbers)
    floor = int(average)
    return min(fuel_sum(floor), fuel_sum(floor + 1))

print(part_two())





