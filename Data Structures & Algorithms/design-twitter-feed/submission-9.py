class Twitter:

    def __init__(self):
        self.count = 0 
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([-self.count, tweetId])

        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)

        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.followerMap[userId].add(userId)

        if len(self.followerMap[userId]) >= 10:
            maxHeap = []
            for f in self.followerMap[userId]:
                if not self.tweetMap[f]:
                    continue

                index = len(self.tweetMap[f])-1
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(maxHeap, [-count, tweetId, f, index-1])

                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)

                while maxHeap:
                    count, tweetId, f, index = heapq.heappop(maxHeap)
                    heapq.heappush(minHeap, [-count, tweetId, f, index-1])
                    
        else:
            for f in self.followerMap[userId]:
                if not self.tweetMap[f]:
                    continue
                index = len(self.tweetMap[f])-1
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(minHeap, [count, tweetId, f, index-1])

                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

            res = []

        while minHeap and len(res) < 10:
            count, tweetId, f, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[f][index]
                heapq.heappush(minHeap, [count, tweetId, f, index-1])

        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
