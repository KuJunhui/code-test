def solution(message, spoiler_ranges):
    words = message.split()
    spoil = set()
    not_spoil = message.split()
    word_index = []
    spoiler_ranges.sort()

    s = 0
    e = -1
    for i, chr1 in enumerate(message):
        if chr1 == ' ' or i == len(message) - 1:
            word_index.append((s, e))
            s = e + 2
        e += 1

    for i, (s, e) in enumerate(word_index):
        for s_range, e_range in spoiler_ranges:
            if e >= s_range and s <= e_range:
                spoil.add(words[i])
                not_spoil.remove(words[i])
                break

    total_w = len(spoil)
    for w in spoil:
        if w in not_spoil:
            total_w -= 1

    return total_w