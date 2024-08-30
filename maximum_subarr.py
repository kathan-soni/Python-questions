def sub_arr_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
result = sub_arr_sum([1,2,3,-1,3])
print(result)
        # here it wil take max value from current element or the element next to it or to the element we get after adding it
        



