# 최소 스패닝 트리 (MST)
# 크루스칼 & 유니온 파인드
def solution(n, costs):
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return True

    # 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    answer = 0
    edge_count = 0

    for a, b, cost in costs:
        if union(a, b):
            answer += cost
            edge_count += 1
            # 섬 n개를 모두 연결하려면 간선은 n-1개 필요
            if edge_count == n - 1:
                break

    return answer

#