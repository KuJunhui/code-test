from collections import Counter

def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합 생성
    def make_bigrams(s):
        s = s.lower()
        bigrams = []
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            # 알파벳 2글자인 경우만 유효
            if a.isalpha() and b.isalpha():
                bigrams.append(a + b)
        return bigrams

    A = make_bigrams(str1)
    B = make_bigrams(str2)

    # 공집합 처리
    if not A and not B:
        return 65536

    # 다중집합 → 교집합 / 합집합 계산
    c1 = Counter(A)
    c2 = Counter(B)

    # 교집합
    inter = sum((c1 & c2).values())
    # 합집합
    union = sum((c1 | c2).values())

    jaccard = inter / union
    return int(jaccard * 65536)
