from collections import defaultdict

class FrequencyOfElements:

    def __init__(self,arr):
        self.arr=arr

    
    def frequency(self):
        n=len(self.arr)
        freq=defaultdict(int)
        order=[]

        for num in self.arr:
                freq[num]+=1

        for key,value in freq.items():
            order.append((key,value))

        return order


result=FrequencyOfElements([1,2,3,4,5,1,2,3])
print(result.frequency())


        