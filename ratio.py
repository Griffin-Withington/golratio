# GOLDEN RATIO

# 1.61803398875

# 1,1,2,3,5,8,13,21,34,55,89.....



class fib(object):
    def __init__(self, starter, limit):
        self.starter = starter
        self.limit = limit

    def ratio(self):
        lst = [0, self.starter]
        for n in range(2, self.limit):
            lst.append(lst[n-1] + lst[n-2])
        return float(lst[-1])/float(lst[-2])


testcases = input("How many test cases? (enter int)")
limit = input("Length of sequence before calculating ratio? (enter int max 1000)")

for i in range(1, int(testcases) + 1):
    test = fib(i, int(limit))
    print("Sequence start: 0," + str(i) + "..., ratio between nth and (n-1)th term: " + str(test.ratio()))
