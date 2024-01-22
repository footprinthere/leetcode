class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        """
        people[i] = [h_i, k_i]
        -> i번째 사람의 키는 h_i이며, 그보다 앞에는 키가 h_i보다 크거나 같은 사람이 k_i명 있어야 함

        time 84% / space 23%
        """
        queue = []

        # h가 크고 k가 작은 사람부터 배치 -> 나중에 배치될 사람이 정렬을 망칠 걱정을 하지 않아도 됨
        for p in sorted(people, key=lambda p: (-1 * p[0], p[1])):
            queue.insert(p[1], p)
        
        return queue
    

if __name__ == "__main__":
    people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    
    answer = Solution().reconstructQueue(people)
    print(answer)
