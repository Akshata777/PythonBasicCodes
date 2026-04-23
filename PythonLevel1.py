# Check if a number is even or odd
def even_odd():
        num = int(input("Enter your number to check even or odd: "))
        if(num%2==0):
           print("number is even")
        else:
            print("number is odd")
#even_odd()

# Find largest of 3 numbers
def largest_num():
     a = int(input("First Number: "))
     b = int(input("Second Number: "))
     c = int(input("Third Number: "))

     if(a>b and a>c):
          print("a is largest")
     elif(b>c):
          print("b is largest")
     else:
          print("c is largest")
#largest_num()

#Print numbers from 1 to 100
def num():
     for i in range(1, 101):
          print(i)
#num()
          
#Print numbers from 100 to 1
def num1():
     for i in range(100, 0, -1):
          print(i)
#num1()

# Find sum of first n numbers
def sum_num():
     num = int(input("Enter number: "))
     total = 0
     for i in range(1, num+1):
          total += i
     print(total)
#sum_num()

#Swap two numbers (without using third variable)
def swap_num():
    a = 10
    b = 20

    a = a + b #10+20=30
    b = a - b #30-20=10
    a = a - b #30-10=20

    print("swapped numbers a: ", a, "b: ", b)
# swap_num()

#Find factorial of a number (loop)
def fact_no():
     num = 5
     fact = 1
     for i in range(1, num+1):
          fact *= i
    
     print("factorial of num: ",fact)
#fact_no()    

     






