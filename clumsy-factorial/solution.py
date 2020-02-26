from operator import add, sub, mul, truediv 
class Solution:

    def clumsy(self, N: int) -> int:
        N, value = N + 1, N - 1 
        store = []
        ops = [sub, mul, truediv, add]
        
        # Normalize list to -> sum/
        for n in range(1,N):
            num = (N - n)
            next_num = (num - 1)
            if num > 1:
                if (n % 4) in [0, 3]:
                    store.append(value)
                    value = next_num
                else:
                    value = int(ops[(n % 4)](value, next_num))
            else:
                store.append(value)

        # Calculate value
        value = store[0]
        for x in range(len(store) - 1):
            if (x % 2) == 0:
                value = value + store[x + 1]
            else:
                value = value - store[x + 1]
        return value

test = Solution()
print(test.clumsy(10))
