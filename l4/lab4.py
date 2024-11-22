import re

inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}

def transform_number(num):
    is_negative = num[0] == '-'
    if is_negative:
        num = num[1:]
    digit_count = {}
    for d in num:
        digit_count[d] = digit_count.get(d, 0) + 1
    trans = []
    for d in num:
        if digit_count.get(d, 0) > 1 and d in inter:
            trans.append(inter[d])  
        else:
            trans.append(d)  
    result = ''.join(trans)
    if is_negative:
        result = '-' + result 
    return result
def proc(path):
    octmin = r'(?:^|\s)-?3[0-7]+(?=\s|$)'
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            valid_matches = re.findall(octmin, line)
            transformed_matches = [transform_number(match) for match in valid_matches]
            if transformed_matches:
                res.append(' '.join(transformed_matches))
    for r in res:
        print(r.strip())
proc('inp.txt')
