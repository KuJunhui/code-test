import re

def solution(files):
    parsed = []
    for file in files:
        # HEAD(숫자 아닌 부분) + NUMBER(연속된 숫자 1~5자리) + TAIL(나머지)
        m = re.match(r'([^0-9]+)([0-9]{1,5})(.*)', file)
        head, number, tail = m.group(1), m.group(2), m.group(3)
        parsed.append((head.lower(), int(number), file))

    parsed.sort(key=lambda x: (x[0], x[1]))  # stable sort => 같은 키면 입력순 유지
    return [x[2] for x in parsed]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))