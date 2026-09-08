class TimeMap:

    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timestamps:
            self.timestamps[key].append((timestamp, value))
        else:
            self.timestamps[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""
            
        array = self.timestamps[key]

        l,r = 0, len(array)-1
        res = None

        while l <= r:
            n = (l+r) // 2
            
            if array[n][0] <= timestamp:
                res = array[n]
                l = n+1

            else:
                r = n-1

        return res[1] if res else ""
