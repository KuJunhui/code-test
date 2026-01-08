from collections import Counter

def solution(str1, str2):
    def multiset(str):
        low_s = str.lower()
        lst = []
        for i in range(len(low_s) - 1):
            if low_s[i].isalpha() and low_s[i + 1].isalpha():
                lst.append(low_s[i] + low_s[i + 1])
        return lst

    lst1 = multiset(str1)
    lst2 = multiset(str2)

    # 공집합 처리
    if not lst1 and not lst2:
        return 65536

    c1 = Counter(lst1)
    c2 = Counter(lst2)
    inter = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    jakard_rate = inter/union

    return int(jakard_rate * 65536)