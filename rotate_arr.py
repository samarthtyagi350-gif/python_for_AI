"""This implementation rotates an array to the right by k positions using the efficient in-place reverse algorithm.

The algorithm works by reversing the entire array first, then reversing the first k elements, and finally reversing the remaining elements. This ensures that the last k elements are moved to the front while maintaining the correct order of all elements.

This approach is optimized because it performs the rotation in-place without using any extra memory.

Time Complexity: O(n)
Space Complexity: O(1)"""



class Rotate_arr:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k
        self.rotate()



    def reverse(self,left,right):
        while left<right:
            self.arr[left],self.arr[right]=self.arr[right],self.arr[left]
            left+=1
            right-=1

    def rotate(self):   
        n=len(arr) 
        k=self.k%n
        self.reverse(0,n-1)
        self.reverse(0,k-1)
        self.reverse(k,n-1)
    
    def display(self):
        return self.arr



arr=list(map(int,input().split()))
k=int(input())
result=Rotate_arr(arr,k)

print(*result.display())