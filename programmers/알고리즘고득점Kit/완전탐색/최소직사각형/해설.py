def solution(sizes):
    sizes = [(max(w, h), min(w, h)) for w, h in sizes]
    return max(w for w, h in sizes) * max(h for w, h in sizes)
