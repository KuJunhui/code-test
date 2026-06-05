def solution(message, spoiler_ranges):
    n = len(message)
    words = message.split()
    w_ranges = []

    s = 0
    e = -1
    for idx, chr1 in enumerate(message):
        if idx == n - 1:
            w_ranges.append((s, idx))
        elif chr1 == ' ':
            w_ranges.append((s, e))
            s = e + 2
        e += 1

    spoil_words = set()
    not_spoil_words = words.copy()
    for idx, (w_s, w_e) in enumerate(w_ranges):
        for s, e in spoiler_ranges:
            if s <= w_e and e >= w_s:
                spoil_words.add(words[idx])
                not_spoil_words.remove(words[idx])
                break

    spoil_words -= set(not_spoil_words)

    return len(spoil_words)
