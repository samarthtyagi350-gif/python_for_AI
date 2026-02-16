class Trailing_zeros:

    def __init__(self,n):
        self.n=n

    def trailingZeroes(self):
        count = 0
        while self.n:
            self.n //= 5
            count += self.n
        return count


n=int(input())
ans=Trailing_zeros(n)

print(f"number of trailing zeros in {n} are {ans.trailingZeroes()}")
