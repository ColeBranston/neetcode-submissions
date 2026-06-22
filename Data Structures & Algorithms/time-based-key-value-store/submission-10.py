class TimeMap:

    def __init__(self):
        self.stor = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("Setting Key: ", key, " for value: ", value, " at time: ", timestamp)
        if timestamp in self.stor:
            self.stor[timestamp][key] = value
        else:
            self.stor[timestamp] = {key:value}

        if key in self.timestamps: # because the timestamps collected will always be in ascending values, we can binary search over them to GET the correct values
            self.timestamps[key].append(timestamp)
        else:
            self.timestamps[key] = [timestamp]

            
    def get(self, key: str, timestamp: int) -> str:
        array = self.timestamps.get(key, [])
        if not array or timestamp < array[0]:
            return ""
        index = self.binarySearch(array, timestamp)
        print("returned bs index: ", index)
        return self.stor[array[index]][key]
    
    def binarySearch(self, array, target):
        l,r = 0, len(array)-1        
        while l <= r:
            n = (l+r)//2
            if array[n] < target:
                l = n+1
            elif array[n] > target:
                r = n-1
            else:
                print("returning target exists: ", n)
                return n
        return l-1
        

        