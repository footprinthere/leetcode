class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        
        optimum = float("inf")
        
        packages.sort()

        for supplier in boxes:
            supplier.sort()
            result = calculate_wasted(packages, supplier)

            if 0 <= result < optimum:
                optimum = result

        if optimum < float("inf"):
            return int((optimum - sum(packages)) % (1e9 + 7))
        else:
            return -1
        

def calculate_wasted(packages: list[int], supplier: list[int]) -> int:
    """ packages와 supplier는 모두 정렬된 상태여야 함 """

    if packages[-1] > supplier[-1]:
        return -1   # impossible
    
    result = 0
    idx = 0

    for box in supplier:
        if idx >= len(packages) or box < packages[idx]:
            continue    # 사용할 수 없는 박스

        limit = binary_search(packages, start=idx, target=box)
        result += (limit - idx + 1) * box   # 박스 용량만 계산

        idx = limit + 1
    
    return result


def binary_search(arr: list[int], start: int, target: int) -> int:
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start + 1) // 2    # 길이가 짝수이면 항상 오른쪽을 선택

        if arr[mid] <= target:
            start = mid     # inclusive
        else:
            end = mid - 1
        
    return start


if __name__ == "__main__":
    packages = [2,3,5]
    boxes = [[4,8],[2,8]]

    packages = [19,3,3,16,3,18,5,5,16,18]
    boxes = [[9],[20,14,7],[7,10,13],[12,15,17],[4,8]]

    packages = [1,4,5,2,4]
    boxes = [[7],[8,6],[6]]

    packages = [2, 4, 6, 8]
    boxes = [[2, 4, 6, 8]]

    answer = Solution().minWastedSpace(packages, boxes)
    print(answer)
