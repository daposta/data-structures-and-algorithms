

def reverse_string(str):
    if not str:
        return ''
    return reverse_string(str[1:]) + str[0]


# print(reverse_string('oladapo'))

def is_palindrome(str):
    if len(str) == 0 or len(str) ==1 :
        return True

    if(str[0] == str[-1]):
        return is_palindrome(str[1:len(str)-1])
    return False


# print(is_palindrome('rotor'))
# result = ''
def convert_decimal_to_binary(decimal,result):
    
    if decimal == 0:
         return result

    result  = (str(decimal%2)) + result
    # print(result)
    return (convert_decimal_to_binary(int(decimal/2), result))

# print(convert_decimal_to_binary(233, ''))


def sum_of_natural_numbers(n):
    if n <= 1 :
        return n
    return (n + sum_of_natural_numbers(n-1))

# print(sum_of_natural_numbers(10))

#binary search is applied to sorted array
def binary_search(arr, x):
    left = 0
    right = len(arr) -1
    if left > right:
        return -1
    mid = int(left +right/2)
    if(x == arr[mid]):
        return mid
    if left < arr[mid]:
        return binary_search(arr[left:mid -1], x)
    return binary_search(arr[mid + 1 :right ], x)


# print(binary_search([1,2,3,4,5,10], 9))

def fibonacci(x ):
    if x == 1 or x ==0:
        return x
    return fibonacci(x - 1) + fibonacci(x-2)

# print(fibonacci(3))

def merge_sort(arr, start, end):
    mid = int((start + end )/2)
    print('end', end)
    print('mid', mid)
    
    #process lhs
    merge_sort(arr, start, mid )
    #process rhs
    merge_sort(arr, mid +1, end)
    #merge data
    merge(arr, start, mid, end)
    return arr


def merge(data, start, mid, end):
    temp_arr = []
    i = start
    j = mid +1
    k = 0
    #merge in sort order if both arrays have values
    while(i <= mid and  j <= end):
        if (data[i] <= data[j]):
            temp_arr[k] = data[i]
            i +=1
            k +=1
        else:
            temp_arr[k] = data[j]
            j+=1
            k+=1
    while(i <= mid ):
        temp_arr[k] = data[i]
        i+=1
        k+=1
    while( j <= end):
        temp_arr[k] = data[j]
        j+=1
        k+=1
    i = start
    while i <= end:
        data[i] = temp_arr[i- start]
        i+=1

x_arr = [9,3,4,5,6,7,1,12]
x_end = len(x_arr)-1
# print('end>>', )
print(merge_sort(x_arr, 0, x_end))