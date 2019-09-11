

# defing linear searching function

#For linear_search funtion
#Time Complexity O(n)
#Sapace Complexity O(1)

def linnear_search(number_list,list_len,searching_number):

    for index in range(list_len):
        if number_list[index] == searching_number:
            return index
    
    # if not found
    return -1 


number_list = [3,4,5,2,5,6,7,8,90,-8,89]

print(linnear_search(number_list, len(number_list),89))
print(linnear_search(number_list, len(number_list),-8))
print(linnear_search(number_list, len(number_list),0))