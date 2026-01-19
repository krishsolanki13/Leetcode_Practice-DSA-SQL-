class Twitter:

    def __init__(self):
        self.count = 0 #Tracks the tweet in time
        self.tweetMap = defaultdict(list) # UserId -> [count, tweetId]
        self.followMap = defaultdict(set) # UserId -> set(userIds)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
 
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId)

        #Initialise the heap with the recent most tweets of the followees
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                lastindex = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][lastindex]
                minheap.append([count, tweetId, followeeId, lastindex - 1])
        
        heapq.heapify(minheap)
        # Heap initialised with the last tweets of the followees
        # Now we populate the res until either res gets full or heap gets empty

        while minheap and len(res) < 10:
            # Pop from the heap and append to res the most recent tweetID
            count, tweetId, followeeId, lastindex = heapq.heappop(minheap)
            res.append(tweetId)
            # Push to the heap next recent tweet for the same followee
            if lastindex >= 0:
                count, tweetId = self.tweetMap[followeeId][lastindex]
                heapq.heappush(minheap, [count, tweetId, followeeId, lastindex - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

