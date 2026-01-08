from collections import deque

def solution(begin, target, words):
    words.append(begin)
    avl_word_set = [set(w[i] for w in words) for i in range(len(words[0]))]
    avl_word_list = [list(_) for _ in avl_word_set]
    visited = [0] * len(words)

    q = deque()
    q.append(len(words) - 1)
    visited[len(words) - 1] = 1

    if target not in words:
        return 0
    while q:
        x = q.popleft()
        if x == words.index(target):
            return visited[x] - 1

        begin_list = ["" + _ for _ in words[x]]

        for i in range(len(avl_word_list)):
            temp_begin_list = begin_list.copy()
            for j in range(len(avl_word_list[i])):
                temp_begin_list[i] = avl_word_list[i][j]
                nx_begin = ""
                for s in temp_begin_list:
                    nx_begin += s
                if nx_begin in words and visited[words.index(nx_begin)] == 0:
                    visited[words.index(nx_begin)] = visited[x] + 1
                    q.append(words.index(nx_begin))
