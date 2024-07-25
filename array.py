# Q find sum of numbers in array and reverse it

nums = input("enter numbers : ")
# This code snippet is taking input numbers from the user, splitting them into individual numbers,
# converting them into integers, and then calculating the sum of all the numbers entered by the user.
nums_li = list(map(int, nums.split()))
sum1 = sum(nums_li)
reverse_list = nums_li[::-1]
print(sum1)
print(reverse_list)

