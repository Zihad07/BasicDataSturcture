

def binary_search(L, x):
    left, right = 0, len(L)-1

    while left<=right:
        mid = (left+right) // 2

        if L[mid] == x:
            return mid
        
        if L[mid] < x:
            left = mid + 1
        else:
            right = mid -1
    

    # if not found 
    return -1


# Checking the binary_search function

if __name__ == '__main__':
    
    L = [1,2,3,5,6,7,8,9]

    for x in range(1,12):
        position = binary_search(L,x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1");
            else:
                print(x, "not in the list.")
        
        else:
            if L[position] == x:
                print(x, "found in the correct position")
            else:
                print('binary search returned', position, "for", x, "which is incorrect")