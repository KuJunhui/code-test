def solution(words):
    # Trie를 "배열 + dict"로 구현 (노드 인덱스 기반)
    children = [dict()]   # children[node] = {char: next_node}
    cnt = [0]             # cnt[node] = 이 노드를 지나가는 단어 수

    def new_node():
        children.append({})
        cnt.append(0)
        return len(children) - 1

    # 1) 단어 삽입하면서 prefix count 누적
    for w in words:
        node = 0
        for ch in w:
            nxt = children[node].get(ch)
            if nxt is None:
                nxt = new_node()
                children[node][ch] = nxt
            node = nxt
            cnt[node] += 1

    # 2) 각 단어별로 "확정되기까지 필요한 입력 글자 수" 합산
    total = 0
    for w in words:
        node = 0
        typed = 0
        for ch in w:
            node = children[node][ch]
            typed += 1
            if cnt[node] == 1:   # 이 접두사는 이 단어만 가지므로 여기서 확정
                break
        total += typed

    return total
