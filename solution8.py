import common
import collections

lines = common.get_lines(__file__)

def process_line(line):
    p1, p2 = l.split('|')
    digits = p1.strip().split()
    output = p2.strip().split()
    return (digits, output)

def part_one():
    count = 0
    lens = (2, 3, 4, 7) # lens for 1, 7, 4, 8
    for l in lines:
        _, output = process_line(l)
        count += sum(1 for c in output if len(c) in lens)
    return count


#### part two

def get_counter(digits):
    counter = collections.Counter()
    for key in digits: counter.update(key)
    return counter

def get_converted_key(key, counter):
    return ''.join(sorted(str(counter.get(c)) for c in key))

numbers = {
    'abcefg' : 0, #6d
    'cf' : 1,  #2
    'acdeg' : 2, #5
    'acdfg' : 3, #5 
    'bcdf' : 4, #4
    'abdfg' : 5, #5
    'abdefg' : 6, #6
    'acf': 7, #3
    'abcdefg' : 8, #7, 86874
    'abcdfg' : 9 #6
}

counter = get_counter(numbers.keys())
# print(counter) # {'f': 9, 'a': 8, 'c': 8, 'g': 7, 'd': 7, 'b': 6, 'e': 4}
mapping = {}
for key, v in numbers.items():
    mapping[get_converted_key(key, counter)] = v


result = 0
for l in lines:
    digits, output = process_line(l)
    counter = get_counter(digits)
    number = 0
    for digit in output:
        number = number * 10 + mapping[get_converted_key(digit, counter)]
    result += number

print(result)






