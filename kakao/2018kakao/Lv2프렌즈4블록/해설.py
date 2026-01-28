def solution(m, n, board):
    # board를 가변 2차원 리스트로 변환
    b = [list(row) for row in board]
    removed_total = 0

    while True:
        to_remove = set()

        # 1) 2x2 같은 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                ch = b[i][j]
                if ch == '':  # 빈칸
                    continue
                if b[i][j + 1] == ch and b[i + 1][j] == ch and b[i + 1][j + 1] == ch:
                    to_remove.add((i, j))
                    to_remove.add((i, j + 1))
                    to_remove.add((i + 1, j))
                    to_remove.add((i + 1, j + 1))

        # 더 이상 지울 게 없으면 종료
        if not to_remove:
            break

        # 2) 한꺼번에 지우기
        removed_total += len(to_remove)
        for i, j in to_remove:
            b[i][j] = ''

        # 3) 아래로 떨어뜨리기(열 단위로 압축)
        for j in range(n):
            stack = []
            for i in range(m - 1, -1, -1):
                if b[i][j] != '':
                    stack.append(b[i][j])

            # 아래부터 채우고 나머지는 빈칸
            i = m - 1
            for ch in stack:
                b[i][j] = ch
                i -= 1
            for k in range(i, -1, -1):
                b[k][j] = ''

    return removed_total


# 간단 테스트
if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15