#Check if a number is prime
def is_prime():
    num = int(input("Enter number: "))
    if num <= 1:
        print("Not Prime")
    else:
        isPrime = True
        for i in range(2, num):
            if num%2 == 0:
                isPrime = False
            break
    if isPrime:
        print("Prime")
    else:
        print("Not prime")
#is_prime()

#Print Fibonacci series up to n
def fibonacci():
    n = 10
    num1,num2 = 0, 1
    for i in range(n):
        print(num1, "")
        num1 , num2 = num2, num1 + num2
#fibonacci()

#Reverse a number (e.g., 123 → 321)
def rev_number():
    num = 12345
    rev = 0
    while(num>0):
        rev = rev *10 + num%10
        num = num // 10
    print("Reversed number: " , rev)
#rev_number()

#Check if a number is palindrome
def palindrome():
    num = 12325
    org_num = num
    rev = 0
    while(num>0):
        rev = rev*10 + num%10
        num = num // 10
    if(org_num == rev):
        print("Palindrome")
    else:
        print("Not Palindrome")
#palindrome()

#Check count of a number
def count():
    num = 123456
    count = 0
    # for i in range(len(str(num))):
    #     count+=1
    # print("Length of number: ", count)

    while num>0:
        num//10
        count += 1
    print("Length of number: ", count)
#count()

#Find sum of digits of a number
def sum_digits():
    num = 12345
    sum, count = 0, 0
    while num > 0:
        sum = num%10
        count = count+sum
        num = num//10
    print("sum of digits: ", count)
#sum_digits()

#Print multiplication table of a number
def multi_num():
    num = 7
    multiply = 0
    for i in range(1, 11):
        multiply = num*i
        print(multiply)
multi_num()


    

