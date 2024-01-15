""" FAILED """

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # 압축
        length, count_list = compress(s)

        # count가 적은 것부터 정렬
        count_list.sort()

        for count in count_list:
            # # 기회 소진 후 종료
            # if k == 0:
            #     break
            
            # 2개 이하이면 효율 1
            if count <= 2:
                if count <= k:
                    k -= count
                    length -= count
                else:
                    length -= k
                    break
            
            # 1개로 줄일 수 있을 때
            elif count - k == 1:
                length -= 1
                break

            # 모두 지울 수 있을 때
            elif count - k <= 0:
                k -= count
                length -= 2
                if k == 0:
                    break
            
            else:
                break

        return length
    

def compress(s: str) -> tuple[int, list[int]]:
    """
    압축 후의 길이와 count들의 list 반환
    """
    length = 0
    prev_ch = ""
    count = 0
    count_list = []

    for ch in s:
        # 같은 문자 출현 -> count 증가
        if ch == prev_ch:
            count += 1
            continue

        # 다른 문자 출현 -> count 반영
        length += 1
        if count > 0:
            count_list.append(count)
            if count > 1:
                length += len(str(count))
        prev_ch = ch
        count = 1

    # 마지막 count 반영
    if count > 0:
        count_list.append(count)
        if count > 1:
            length += len(str(count))

    return length, count_list


"""
# IDEA

* 여러 개인 문자를 모두 지울 때 -> 2 절약
    - 만약 2개 있다면 효율 1
    - 2개보다 많다면 효율 <1
* 여러 개인 문자를 1개로 줄일 때 -> 1 절약
    - 만약 2개 있다면 효율 1
    - 2개보다 많다면 효율 <1
* 하나 있던 문자를 지울 때 -> 1 절약

* 각 문자의 개수가 중요 -- counter 이용 필요
    1순위: 1개 또는 2개짜리
    2순위: 나머지 (1개 이하로 줄이지 못하면 무의미)

---

* 단순 counter 안 되고, 이웃하는 것들끼리만 세야 함

---

* 이웃하지 않던 것이 이웃하게 되는 경우 고려해야 함 (예: aabaa -> aaaa)
    - 이때 효율이 1보다 커질 수 있음
    - 이건 count <= k일 때만 고려하면 됨
* merge 가능할 때 효율을 쉽게 예측할 수 있을까?
* 아니면 BFS 식으로 여러 가능성을 비교해야 할까? -> 그러면 너무 많아질 듯

* count가 2자리 이상인 경우 고려 필요
    0순위: merge로 1보다 큰 효율을 낼 수 있을 때
    1순위: 1개 또는 2개짜리
    2순위: 나머지 (1개 이하로 줄이지 못하면 무의미)
        - 자릿수만큼 줄어듦
"""


if __name__ == "__main__":
    # s = "aaabcccd"
    # k = 2

    s = "aabbaa"
    k = 2

    answer = Solution().getLengthOfOptimalCompression(s, k)
    print(answer)
