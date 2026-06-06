import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.users_tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users_tweets:
            self.users_tweets[userId] = []
        self.time += 1
        self.users_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        user_list = list(self.following.get(userId, set()))
        user_list.append(userId)
        for u_id in user_list:
            if u_id in self.users_tweets and self.users_tweets[u_id]:
                tweets = self.users_tweets[u_id]
                last_idx = len(tweets) - 1
                time, tweetId = tweets[last_idx]
                max_heap.append((time, tweetId, u_id, last_idx - 1))

        heapq.heapify_max(max_heap)

        while max_heap and len(res) < 10:
            time, tweetId, u_id, next_idx = heapq.heappop_max(max_heap)
            res.append(tweetId)

            if next_idx >= 0:
                next_time, next_tweetId = self.users_tweets[u_id][next_idx]

                heapq.heappush_max(
                    max_heap, (next_time, next_tweetId, u_id, next_idx - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
