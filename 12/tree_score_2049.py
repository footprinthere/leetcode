from collections import deque, Counter


class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        """time 99 / space 99"""

        N = len(parents)
        size = [1] * N
        # sizes[n] : Size of subtree with root n
        prod_down = [1] * N
        # prod_down[n] : Product of sizes of n's children
        inorder = Counter(parents[1:])
        # inorder[n] : # of n's children

        queue = deque([n for n in range(N) if n not in inorder])
        # Initialized with leaf nodes

        while queue:
            node = queue.popleft()

            p = parents[node]
            if p > -1:
                size[p] += size[node]
                prod_down[p] *= size[node]

            inorder[p] -= 1
            if inorder[p] == 0:
                # All children of p are already visited
                queue.append(p)

        # Now score = prod_down[n] * (sizes[0] - sizes[n])
        S = size[0]
        max_score = prod_down[0]
        max_count = 1

        for n in range(1, N):
            score = prod_down[n] * (S - size[n])
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1

        return max_count


if __name__ == "__main__":
    parents = [-1, 2, 0, 2, 0]  # 3
    parents = [-1, 2, 0]  # 2

    parents = [-1, 3, 3, 5, 7, 6, 0, 0]  # 2

    answer = Solution().countHighestScoreNodes(parents)
    print(f"{answer = }")
