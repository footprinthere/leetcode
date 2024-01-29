from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        """ time 78% / space 93% """
        graph = CourseGraph(relations, time)
        return graph.topo_sort()


class CourseGraph:
    def __init__(self, relations: list[list[int]], time: list[int]):
        self.adj = defaultdict(list)
        self.inorder = defaultdict(int)

        for src, trg in relations:
            self.adj[src].append(trg)
            self.inorder[trg] += 1

        self.time = [-1] + time             # 1부터 시작
        self.intime = [0] * len(self.time)  # 직전 node들까지의 누적시간

    def topo_sort(self) -> int:
        zero_q: deque[int] = deque([
            course for course in range(1, len(self.time))
            if self.inorder[course] == 0
        ])

        while zero_q:
            course = zero_q.popleft()

            # 직전 node들 중 가장 오래 걸리는 것을 time에 반영
            self.time[course] += self.intime[course]

            # 다음 node로 이동
            for trg in self.adj[course]:
                # intime 업데이트
                self.intime[trg] = max(self.intime[trg], self.time[course])

                self.inorder[trg] -= 1
                if self.inorder[trg] == 0:
                    zero_q.append(trg)

        return max(self.time)


if __name__ == "__main__":
    # n = 3
    # relations = [[1,3],[2,3]]
    # time = [3,2,5]

    # n = 5
    # relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
    # time = [1,2,3,4,5]
    
    n = 7
    relations = [[1,7],[1,4],[1,3],[2,3],[4,3],[5,3],[7,3],[7,6]]
    time = [6,5,1,8,2,9,4]

    answer = Solution().minimumTime(n, relations, time)
    print(answer)
