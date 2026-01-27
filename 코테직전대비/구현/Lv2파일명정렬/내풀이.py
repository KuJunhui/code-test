import re

def solution(files):
    answer = []
    for file in files:
        m = re.match(r'([^0-9]+)([0-9]{1,5})(.*)', file)
        head, number, tail = m.group(1), m.group(2), m.group(3)
        answer.append((head.lower(), int(number), file))

    answer.sort(key=lambda x : (x[0], x[1]))
    return [a[2] for a in answer]