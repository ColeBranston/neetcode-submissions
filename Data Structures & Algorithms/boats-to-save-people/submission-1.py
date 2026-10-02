class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l,r = 0, len(people)-1

        print(people)

        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1

            else:
                res += 1
                r -= 1

        return res