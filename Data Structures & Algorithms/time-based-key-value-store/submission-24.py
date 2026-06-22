class TimeMap:

    def __init__(self):
        self.store = {}  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        l, r = 0, len(arr) - 1
        if timestamp < arr[0][0]:
            return ""

        if len(arr) == 1:
            return arr[0][1]

        while l <= r:
            mid = (l + r) // 2

            if timestamp > arr[mid][0]:
                l = mid+1

            elif timestamp < arr[mid][0]:
                r = mid-1

            else:
                return arr[mid][1]
        print(arr)
        return arr[l-1][1]