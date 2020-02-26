class Solution:
    def clumsy(self, N: int) -> int:

        N = N + 1
        value = N - 1
        store = []
        ops = {
            1: lambda x,y: x * y,
            2: lambda x,y: x / y,
            3: lambda x,y: x + y,
            0: lambda x,y: x - y, 
        }

        for n in range(1,N):

            num = (N - n)
            next_num = (num - 1)
            if num > 1:
                #normalize list
                if (n % 4) in [0,3]:
                    store.append(value)
                    value = next_num
                else:
                    value = int(ops[(n % 4)](value, next_num))
            else:
                store.append(value)

        # SUM -> this can be converted to a list comprehension

        value = store[0]
        for x in range(len(store)):
            if x < (len(store) - 1):
                if (x % 2) == 0:
                    value = int(value + store[x + 1])
                else:
                    value = int(value - store[x + 1])

        return value
