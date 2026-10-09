class Solution:
    def fib_recursive(self, n):

        def fib(f):
            if f == 0:
                return 0

            if f == 1:
                return 1

            return fib(f - 1) + fib(f - 2)

        for i in range(n):
            print(fib(i))

    def fib_iterative(self, n):
        a = 0
        b = 1

        for i in range(n):
            print(a)
            a, b = b, a + b

if __name__ == "__main__":
    sol = Solution()

    print("Recursive:")
    sol.fib_recursive(7)

    print("Iterative:")
    sol.fib_iterative(7)