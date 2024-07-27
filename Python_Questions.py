# pattern Questions (1) :

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=' ') # this loop will run until condition
#     print() # this for putting them in next line thats why out of j loop





# pattern questions (2)

# for i in range(1, 6):
#     for j in range(5, i, -1):
#         print(" " ,end= " ")
#     for k in range(1, i+1):
#         print(k , end=' ')
#     for m in range(i-1 , 0 , -1):
#         print(m , end=' ')   
#     print() 





# Q3 Check number is armstrong or not?

# n = int(input("enter number check it is armstrong or not: "))
# n_str = str(n)
# n_len = len(n_str)
# sum_digits = 0
# for i in n_str: # here number suppose is 100 so first i will have 1 with index 0. 
#     sum_digits += int(i) ** n_len
# if sum_digits == n:
#     print(n, "armstrong hai")
# else:
#     print(n, "tu armstrong nahi hai bornvita piya kar")
    
    




# Q4 find sum of numbers in array and reverse it

# nums = input("enter numbers : ")
# # This code snippet is taking input numbers from the user, splitting them into individual numbers,
# # converting them into integers, and then calculating the sum of all the numbers entered by the user.
# nums_li = list(map(int, nums.split()))
# sum1 = sum(nums_li)
# print(sum1)







#Q5 Reverse the array :

# nums = input("enter string : ")
# nums_list = list(map(str, nums.split()))
# reverse_list = nums_list[::-1]
# print(reverse_list)


# def check_divisibility(a, b):
#     if b %a ==0:
#         print("good")
#     else:
#         print("noo never")
# sum = check_divisibility(10, 21)








# Q6 keep entering number from user until it enter -1 use while loop 


# a = []
# sum = 0 
# while True:
#     try: # this will help in checking if the input is in another format it will give a message
#         user = int(input("enter the numbers :"))
#         if user <= -1:
#             print(f"{user} can't be printed")
#             for i in range(0, len(a)):
#                 sum += a[i]
#             print(f"Total sum of all integers in the array is {sum}")
#             break
#         a.append(user)
#         print(a)
#     except ValueError:
#         print("please enter correct integer") # this is the message that will be highlighted and again while loop will start and user will enter the numbers


