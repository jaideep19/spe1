



 

  

def kthDiff(n,l, k): 
    from bisect import bisect as upper_bound
    l.sort()
    low = l[1] - l[0] 
    for i in range(1, n - 1): 
        low = min(low, l[i + 1] - l[i])   
    high = l[n - 1] - l[0] 
    while (low < high): 
        print(mid)
        mid = (low + high) >> 1
        if(sum([upper_bound(l, l[i] + mid) for i in range(n)])<k ):
            low = mid + 1
        else: 
            high = mid 
  
    return low 
print(kthDiff(3,[1,2,3],7))