def solution(clothes):
    categories = {}
    for name, category in clothes:
        categories[category] = categories.get(category, 0) + 1

    answer = 1
    for count in categories.values():
        answer *= (count + 1)

    return answer - 1