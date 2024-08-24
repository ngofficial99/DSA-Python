def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    
    a.sort()
    # if n == 0 or n == 1:
    # print(-1, -1)

    SecondSmallest = a[1]
    SecondLargest = a[n-2]

    return([SecondLargest,SecondSmallest])

    getSecondOrderElements(n,a)
   
