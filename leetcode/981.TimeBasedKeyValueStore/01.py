class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps = self.cache.get(key)
        if timestamps is None:
            timestamps = {}
        timestamps[timestamp] = value
        self.cache[key] = timestamps

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.cache.get(key)
        if timestamps is None:
            return ''
        mostRecentTimestamp = self.getMostRecentTimestamp(list(timestamps.keys()), timestamp)
        if mostRecentTimestamp is None:
            return ''
        return timestamps.get(mostRecentTimestamp)

    def getMostRecentTimestamp(self, timestampList, target: int) -> int | None:
        left, right = 0, len(timestampList) - 1

        while left <= right:
            mid = (left + right) // 2
            value = timestampList[mid]
            if value == target:
                return target
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        if left == 0:
            return None
        return timestampList[left - 1]
