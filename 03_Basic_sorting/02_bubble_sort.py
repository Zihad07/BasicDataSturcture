
def bubble_sort(L):

    n = len(L)

    operation_cnt = 0
    for i in range(n):
        

        for j in range(0, n-i-1):
        # for j in range(0, n-1):
            operation_cnt += 1 

            if L[j] > L[j+1]:
                # swap
                L[j], L[j+1] = L[j+1], L[j]

        
        print('step-',i+1,':',L)
    
    return operation_cnt



# ----------------------------------------------------------

if __name__ == '__main__':

    L = [6,1,4,9,2]
    # L = [6,1,4,9,2,8,0,9,9,12,-1,4]

    print('Befor sort:', L)

    noof_operation = bubble_sort(L)
    print('Number of operation:',noof_operation)
    

    print('After sort:',L)