class Merging:
    def merge(self, nums1, m, nums2, n):

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1


nums1=list(map(int,input().split()))
m=int(input())

nums2=list(map(int,input().split()))
n=int(input())

result=Merging()
print(*(result.merge(nums1,m,nums2,n)))