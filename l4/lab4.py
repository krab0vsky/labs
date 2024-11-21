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
    ch = 0
    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
            ch+=1
        else:
            trans.append(d)
            dc[d] = 1
    if ch > 0:
        return ''.join(trans)
    else: return ''.join('')

def proc(path):
    octmin = r'\b3[0-7]+\b'
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            
            for m in re.finditer(octmin,line):
                transformed_line = re.sub(octmin, transform_number, m[0])
                res.append(transformed_line)


    for r in res:
        print(r,end=" ")

proc('inp.txt')

