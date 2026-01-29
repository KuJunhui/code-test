def solution(words):
    children = [dict()]
    cnt = [0]

    def new_node():
        children.append({})
        cnt.append(0)
        return len(children) - 1

    for w in words:
        node = 0
        for ch in w:
            nxt = children[node].get(ch)
            if nxt is None:
                nxt = new_node()
                children[node][ch] = nxt
            node = nxt
            cnt[node] += 1

    total = 0
    for w in words:
        node = 0
        typed = 0
        for ch in w:
            node = children[node][ch]
            typed += 1
            if cnt[node] == 1:
                break
        total += typed

    return total
