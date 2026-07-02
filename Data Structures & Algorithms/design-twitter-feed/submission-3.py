from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([-self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.followMap[userId].add(userId)

        if len(self.followMap[userId]) >= 10:
            maxHeap = []

            for followerId in self.followMap[userId]:
                if not self.tweetMap[followerId]:
                    continue

                index = len(self.tweetMap[followerId]) - 1
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(maxHeap, [-count, tweetId, followerId, index - 1])

                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)

            while maxHeap:
                count, tweetId, followerId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followerId, index])

        else:
            for followerId in self.followMap[userId]:
                if not self.tweetMap[followerId]:
                    continue

                index = len(self.tweetMap[followerId]) - 1
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])

        output = []

        while minHeap and len(output) < 10:
            count, tweetId, followerId, index = heapq.heappop(minHeap)
            output.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followerId][index]
                heapq.heappush(minHeap, [count, tweetId, followerId, index - 1])

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)