def solution(message, spoiler_ranges):
    words = message.split()
    spoil = set()
    not_spoil = []

    word_index = []
    n = len(message)
    i = 0

    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        s = i
        while i < n and message[i] != ' ':
            i += 1
        e = i - 1
        word_index.append((s, e))

    for i, (s, e) in enumerate(word_index):
        is_spoil = False
        for s_range, e_range in spoiler_ranges:
            if e >= s_range and s <= e_range:
                spoil.add(words[i])
                is_spoil = True
                break
        if not is_spoil:
            not_spoil.append(words[i])

    total_w = len(spoil)
    for w in spoil:
        if w in not_spoil:
            total_w -= 1

    return total_w