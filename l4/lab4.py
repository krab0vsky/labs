import re

inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}


def transform_number(match):
    num = match.group(0)
    dc = {}
    trans = []
    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
        else:
            trans.append(d)
            dc[d] = 1

    return ''.join(trans)

def proc(path):
    octal_number_pattern = r'\b3[0-7]+\b'
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            # Заменяем каждое восьмеричное число, подходящее под условия
            transformed_line = re.sub(octal_number_pattern, transform_number, line)
            res.append(transformed_line.strip())
    for r in res:
        print(r)

proc('l4/inp.txt')