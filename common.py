import os  
import re

def get_lines(file):
    part = re.search('\d+', os.path.basename(file))
    if part:
        inputFile = f"input{part.group()}.txt"
        with open(inputFile) as f: lines = f.readlines()
        return [l.strip() for l in lines]
    else:
        raise ValueError('solution script has to be ends with num-num')


def get_nums(file):
    strs = get_lines(file)
    return [int(s) for s in strs]