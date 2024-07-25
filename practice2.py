# # # python practice 
# # # = is for assigning a value to a variable
# # for i in range(10): # starting is from 0 to 9 or if we write 1 to 10 then also 10 will be excluded
# #     print(str(i)+ ".kathan soni") # here we have to use , not + to add variable with string


# # num1 = int(input("enter number 1: "))    
# # num2 = int(input("enter number 2: "))  
# # res = num1 + num2
# # print(res)  

# # num = int(input("enter number : "))
# # for i in range(1, 11):
# #     print(str(num) + "X" + str(i) + "=" + str(num*i))

# # sum = 0
# # for num in range(0,11):
# #     sum = sum + num
# #     print(sum) # it will show the sum of each numbers
# # print(sum) # directly show the sum 

# # fact = 1
# # num = int(input("enter number : "))
# # for i in range(1, num+1):
# #     fact = fact * i 
# # print(fact)

# # pattern Questions:

# # for i in range(1, 6):
# #     for j in range(1, i+1):
# #         print(j, end=' ') # this loop will run until condition
# #     print() # this for putting them in next line thats why out of j loop


# # for i in range(1, 6):
# #     for j in range(5, i, -1):
# #         print(" " ,end= " ")
# #     for k in range(1, i+1):
# #         print(k , end=' ')
# #     for m in range(i-1 , 0 , -1):
# #         print(m , end=' ')   
# #     print() 


# # Q Check number is armstrong or not?

# # n = int(input("enter number check it is armstrong or not: "))
# # n_str = str(n)
# # n_len = len(n_str)
# # sum_digits = 0
# # for i in n_str: # here number suppose is 100 so first i will have 1 with index 0. 
# #     sum_digits += int(i) ** n_len
# # if sum_digits == n:
# #     print(n, "armstrong hai")
# # else:
# #     print(n, "tu armstrong nahi hai bornvita piya kar")
    
    
# # Q find sum of numbers in array and reverse it

# # nums = input("enter numbers : ")
# # # This code snippet is taking input numbers from the user, splitting them into individual numbers,
# # # converting them into integers, and then calculating the sum of all the numbers entered by the user.
# # nums_li = list(map(int, nums.split()))
# # sum1 = sum(nums_li)
# # print(sum1)

# #Q Reverse the array :

# # nums = input("enter string : ")
# # nums_list = list(map(str, nums.split()))
# # reverse_list = nums_list[::-1]
# # print(reverse_list)


# # def check_divisibility(a, b):
# #     if b %a ==0:
# #         print("good")
# #     else:
# #         print("noo never")
# # sum = check_divisibility(10, 21)
# import math
# # Q prime number
# # Define the upper limit
# n = 100

# list = []
# # Iterate over numbers from 2 to n (100)
# for i in range(2, n + 1):
#     is_prime = True  # Assume the number is prime

#     # Check for factors from 2 to i / 2
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:
#             is_prime = False  # Number is not prime
#             break
    
#     # Print the number if it's prime
#     if is_prime:
#         list.append(i)

# print(list)

# Q keep entering number from user until it enter -1 use while loop 


a = []
sum = 0 
while True:
    try: # this will help in checking if the input is in another format it will give a message
        user = int(input("enter the numbers :"))
        if user <= -1:
            print(f"{user} can't be printed")
            for i in range(0, len(a)):
                sum += a[i]
            print(f"Total sum of all integers in the array is {sum}")
            break
        a.append(user)
        print(a)
    except ValueError:
        print("please enter correct integer") # this is the message that will be highlighted and again while loop will start and user will enter the numbers


