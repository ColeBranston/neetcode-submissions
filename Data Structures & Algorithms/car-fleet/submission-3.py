class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # not backtracking

        # zip the two arrays together than sort by position
            # find the difference between the last element and the target and pop it if the 
        
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x:x[0])

        for i in range(len(cars)):
            cars[i] += ((target - cars[i][0]) / cars[i][1],)
            
        counter = 1

        print(cars)
        prev = cars.pop()[2]

        while cars:
            temp = cars.pop()[2]
            print("temp: ", temp, "prev: ", prev)
            
            if prev >= temp:
                pass

            else:
                counter += 1
                prev = temp
            
        return counter




