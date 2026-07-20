class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(prefix):
            # Count how many numbers start with this prefix
            total = 0
            curr = prefix
            next_prefix = prefix + 1

            while curr <= n:
                total += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10

            return total

        curr = 1
        k -= 1  # because we start at 1

        while k > 0:
            steps = count(curr)

            if steps <= k:
                # Skip this whole subtree
                curr += 1
                k -= steps
            else:
                # Go deeper into this subtree
                curr *= 10
                k -= 1

        return curr