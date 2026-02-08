import numpy as np

class FlattenList:
    def __init__(self,arr):
        self.arr=arr

    def flatten(self):
        return self.arr.flatten()
    



arr=np.array([[1,2],[3,4],[5,6]])
result=FlattenList(arr)
print(result.flatten())
        