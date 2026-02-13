class pow_of_two:

    def __init__(self,n):
        self.n=n
        
    def isPowerOfTwo(self):
        if self.n <= 0:
            return False
        
        return (n & (n - 1)) == 0
    


n=int(input())
result=pow_of_two(n)

print(result.isPowerOfTwo())



