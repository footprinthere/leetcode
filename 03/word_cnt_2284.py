from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        """ time 98% / space 12% """
        
        word_counts = defaultdict(int)

        for message, sender in zip(messages, senders):
            word_count = len(message.split(" "))
            word_counts[sender] += word_count

        # count가 가장 큰 사람 골라내기
        candidates = []
        max_count = 0

        for sender, word_count in word_counts.items():
            if word_count > max_count:
                # 기록 갱신 -> candidates 초기화
                candidates = [sender]
                max_count = word_count
            elif word_count == max_count:
                # 동일 기록 -> candidates에 추가
                candidates.append(sender)

        # 여러 명이면 lexicographically largest 선택
        return max(candidates)
    
    def short(self, messages: list[str], senders: list[str]) -> str:
        """ time 89% / space 26% """

        word_counts = defaultdict(int)

        for message, sender in zip(messages, senders):
            word_counts[sender] += len(message.split())

        # 정렬 기준이 여러 개일 때 tuple 활용하기!
        return max(senders, key=lambda s: (word_counts[s], s))
    

if __name__ == "__main__":
    # messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
    # senders = ["Alice","userTwo","userThree","Alice"]

    messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
    senders = ["Bob","Charlie"]

    answer = Solution().largestWordCount(messages, senders)
    print(answer)
