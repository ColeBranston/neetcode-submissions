class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target-position / speed[i] gives the time until reaching the destination

        stack = []
        prev = None

        cars = sorted(zip(position, speed))

        for car in cars:
            time = (target-car[0]) / car[1]
            stack.append(time)

        first = stack.pop()
        res = [first]
        prev = first

        while stack:
            nextCar = stack.pop()
            if nextCar > prev:
                res.append(nextCar)
                prev = nextCar

        return len(res)
