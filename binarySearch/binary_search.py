def binarySearch(a, key):
    left = 0
    right = len(a)
    while left < right:
        mid = left + (right-left) // 2
        
        if a[mid] == key:
            return f"found at {mid}"
        elif a[mid] > key:
            right = mid
        else:
            left = mid + 1
        
        return "Not Found"
            

