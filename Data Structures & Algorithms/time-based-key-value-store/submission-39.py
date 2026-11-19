class TimeMap:

    def __init__(self):
        self.names = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.names[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        array = self.names[key]
        l,r = 0, len(array)-1

        if not array:
            return ""

        res = array[0][0] if timestamp >= array[0][1] else ""

        while l <= r:
            n = (l+r) // 2

            if array[n][1] < timestamp:
                l = n + 1
                res = array[n][0]

            elif array[n][1] > timestamp:
                r = n - 1

            else:
                return array[n][0]

        return res

