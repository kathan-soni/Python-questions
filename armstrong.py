# Q Check number is armstrong or not?

n = int(input("enter number check it is armstrong or not: "))
n_str = str(n)
n_len = len(n_str)
sum_digits = 0
for i in n_str: # here number suppose is 100 so first i will have 1 with index 0. 
    sum_digits += int(i) ** n_len
if sum_digits == n:
    print(n, "hurray you are armstrong number")
else:
    print(n, "sorry buddy you are not a armstrong number")