class FindingMaximumDifference:
    def __init__(self,arr):
        self.arr=arr

    
    def maximum_difference(self):

        max_diff=0
        min_diff=self.arr[0]

        for i in range(len(self.arr)):
            if self.arr[i]<min_diff:
                min_diff=self.arr[i]

            else:
                result=self.arr[i]-min_diff
                max_diff=max(max_diff,result)

        
        return max_diff
    

s=FindingMaximumDifference([7,1,5,3,6,4])
print(f"Maximum difference is {s.maximum_difference()}")