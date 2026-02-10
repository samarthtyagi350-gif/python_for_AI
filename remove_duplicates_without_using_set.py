class remove_duplicates_without_using_set:
    def __init__(self,arr):
        self.arr=arr
    
    def remove_duplicates(self):
        freq=[0 for i in range(max(self.arr)+1)]
        order=[]

        for num in self.arr:
            if num not in freq:
                freq[num]=1
                order.append(num)

        return order
    


result=remove_duplicates_without_using_set([1,2,1,4,5,1,2,3])
print(result.remove_duplicates())