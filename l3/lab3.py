"""Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом), 
распознает, преобразует и выводит на экран объекты по определенному правилу. 
Объекты разделены пробелами. Преобразование делать по возможности через словарь. 
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. 
Регулярные выражения использовать нельзя.
Натуральные нечетные восьмеричные числа, начинающиеся с 3. Для каждого числа повторяющиеся цифры вывести прописью."""
inter = {
    '1': 'один',
    '3': 'три',
    '5': 'пять',
    '7': 'семь',
}

def valid(word):
    if word[0] == '-':
        word = word[1:]  
    return len(word) > 0 and word[0] == '3' and all('0' <= ch <= '7' for ch in word) and int(word, 8) % 2 == 1

def transform_number(num):
    dc = {}
    trans = []
    ch = 0
    is_negative = num[0] == '-' 
    if is_negative:
        num = num[1:]  

    for d in num:
        if d in dc and d in inter:
            trans.append(inter[d])
            ch += 1
        else:
            trans.append(d)
            dc[d] = 1

    result = ''.join(trans)
    if is_negative:
        result = '-' + result  

    if ch > 0:
        return result
    else:
        return ''

def proc(path):
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split() 
            trans_line = [] 
            for word in words:
                if valid(word):
                    trans_line.append(transform_number(word))
                else:
                    continue
                    
            res.append(' '.join(trans_line))
    for r in res:
        print(r)

proc('inp.txt')
