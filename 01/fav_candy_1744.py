def solution(candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
    cumCount = [candiesCount[0]]
    for count in candiesCount[1:]:
        cumCount.append(cumCount[-1] + count)

    answer = [process(candiesCount, cumCount, query) for query in queries]

    return answer


def process(candiesCount: list[int], cumCount: list[int], query: list[int]) -> bool:
    t, day, cap = query[0], query[1], query[2]

    # type t candy: (cum[t-1] ~ cum[t]]
    prev_cum = cumCount[t-1] if t-1 >= 0 else 0
    # 그날 먹을 수 있는 사탕의 수: [day+1 ~ cap*(day+1)]
    min_eaten, max_eaten = day + 1, cap * (day + 1)

    return prev_cum + 1 <= max_eaten and min_eaten <= cumCount[t]
    

if __name__ == "__main__":
    # count = [46,5,47,48,43,34,15,26,11,25,41,47,15,25,16,50,32,42,32,21,36,34,50,45,46,15,46,38,50,12,3,26,26,16,23,1,4,48,47,32,47,16,33,23,38,2,19,50,6,19,29,3,27,12,6,22,33,28,7,10,12,8,13,24,21,38,43,26,35,18,34,3,14,48,50,34,38,4,50,26,5,35,11,2,35,9,11,31,36,20,21,37,18,34,34,10,21,8,5]
    # query = [[85, 54, 42]]
    count = [7,4,5,3,8]
    query = [[0,2,2],[4,2,4],[2,13,1000000000]]

    solution(count, query)
