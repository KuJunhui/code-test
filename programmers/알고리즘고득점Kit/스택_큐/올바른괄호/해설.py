def solution(s):
    balance = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            if balance == 0:
                return False
            balance -= 1

    return balance == 0
