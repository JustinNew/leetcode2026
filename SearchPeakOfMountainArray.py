def searchPeakOfMountainArray(arr):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]
    
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return arr[right]

print(searchPeakOfMountainArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(searchPeakOfMountainArray([1, 2, 3, 4, 5, 6, 5,3,1]))
print(searchPeakOfMountainArray([1, 2, 1]))
print(searchPeakOfMountainArray([1, 3, 5, 3, 1]))
print(searchPeakOfMountainArray([1]))
print(searchPeakOfMountainArray([]))