def solution(phone_book):
    children = [dict()]
    cnt = [0]

    def new_node():
        children.append({})
        cnt.append(0)
        return len(cnt) - 1

    for phone in phone_book:
        node = 0
        for n in phone:
            nxt = children[node].get(n)
            if not nxt:
                nxt = new_node()
                children[node][n] = nxt
            node = nxt
            cnt[node] += 1

    for phone in phone_book:
        node = 0
        typed = 0
        for n in phone:
            node = children[node].get(n)
            if cnt[node] == 1:
                break
            typed += 1

        if typed == len(phone):
            return False

    return True
