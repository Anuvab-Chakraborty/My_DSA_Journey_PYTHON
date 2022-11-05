from collections import Counter
def mostFrequentEven(nums):
    if len(nums)==1 and nums[0]%2==0:return nums[0]
    if len(nums)==1 and nums[0]%2!=0:return -1
    
    min_ele=float("inf")
    count=float("-inf")
    nums.sort()
    res=Counter(nums)
    for i in res:
        if res[i]>1 and i%2==0:
            #count=max(count,res[i])
            #print(count)
            if count==res[i]:
                min_ele=min(min_ele,i)
                return min_ele
        count=max(res[i],count)
        print(count)
        for key, value in res.items():
            if count == value:return key
    return -1
         


    """
        min_ele=float("inf")
        nums.sort()
        res=Counter(nums)
        print(res)
        for i in res:
            if res[i]>1 and i%2==0:
                min_ele=min(min_ele,i)
        return min_ele
        """
nums=[2,10000,10000,10000,2]
#nums=[1001]
#nums = [29,47,21,41,13,37,25,7]
#nums = [4,4,4,9,2,4]
#nums = [0,1,2,2,4,4,1]
print(mostFrequentEven(nums))
