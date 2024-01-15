from collections import defaultdict, deque


class Solution:
    def sortItems(
        self, n: int, m: int, group: list[int], beforeItems: list[list[int]]
    ) -> list[int]:
        
        # 전체 및 각 gropu의 graph 구성
        # 전체 graph에서 한 group은 (group 번호 + n)의 단일한 node로 취급
        graph = TopoGraph()
        groups = [TopoGraph() for _ in range(m)]

        for i, g in enumerate(group):
            grouped_before = list({
                bi if group[bi] == -1 else group[bi] + n
                for bi in beforeItems[i]
            })
            if g == -1:
                graph.add_node(i, grouped_before)
            else:
                grouped_before = [
                    bi for bi in grouped_before
                    if bi != g + n      # 자신으로 향하는 edge 배제
                ]
                graph.add_node(g + n, grouped_before)

                # group에 속해 있으면 그 group의 graph에도 추가
                in_group_before = [
                    bi for bi in beforeItems[i]
                    if group[bi] == g   # 다른 group에 속하는 것 배제
                ]
                groups[g].add_node(i, in_group_before)

        # 전체 graph에 대해 topo sort 수행
        whole_sorted = graph.topo_sort()
        if len(whole_sorted) == 0:
            return []
        
        # group 내의 순서까지 반영해 최종 순서 산출
        answer = []
        for node in whole_sorted:
            if node < n:
                answer.append(node)
            else:
                group_sorted = groups[node - n].topo_sort()
                if len(group_sorted) == 0:
                    return []
                answer.extend(group_sorted)

        return answer
    

class TopoGraph:
    def __init__(self):
        self.adj = defaultdict(list)
        # self.adj[x] = [y, z, ...] : x->y, x->z, ...
        self.inorder = defaultdict(int)

    def add_node(self, node: int, before: list[int]):
        self.adj[node]  # 없었으면 빈 list로 생성

        for b in before:
            self.adj[b].append(node)
        self.inorder[node] += len(before)

    def topo_sort(self) -> list[int]:
        result = []
        zero_q = deque([
            node for node in self.adj.keys()
            if self.inorder[node] == 0
        ])

        while zero_q:
            node = zero_q.popleft()
            result.append(node)

            for adj in self.adj[node]:
                self.inorder[adj] -= 1
                if self.inorder[adj] == 0:
                    zero_q.append(adj)

        if len(result) == len(self.adj):
            return result
        else:
            return []   # 정렬 불가능


if __name__ == "__main__":
    # n = 8
    # m = 2
    # group = [-1,-1,1,0,0,1,0,-1]
    # beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

    # n = 4
    # m = 1
    # group = [-1,0,0,-1]
    # beforeItems = [[],[0],[1,3],[2]]

    m, n = 5, 5
    group = [2,0,-1,3,0]
    beforeItems = [[2,1,3],[2,4],[],[],[]]

    answer = Solution().sortItems(n, m, group, beforeItems)
    print(answer)
