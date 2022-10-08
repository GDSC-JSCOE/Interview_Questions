
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        maxi = 1
        plat = 1
        while i<n and j < n:
            if arr[i]<=dep[j]:
                plat+=1
                i+=1
            elif arr[i]>dep[j]:
                plat-=1
                j+=1
            if plat>maxi:
                maxi = plat
        return maxi
