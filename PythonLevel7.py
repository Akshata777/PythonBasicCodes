def pattern1():
    for i in range(4):
        for j in range(4):
            print("*",end=" ")
        print()
#pattern1()

def pattern2():
    for i in range(1, 5):
        for j in range(i):
            print("*", end=" ")
        print()
#pattern2()

def pattern3():
    for i in range(1,5):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
#pattern3()

def pattern4():
    for i in range(1,5):
        for j in range(1, i+1):
            print(i, end=" ")
        print()
#pattern4()

def pattern5():
    for i in range(5,1,-1):
        for j in range(i,1,-1):
            print("*", end=" ")
        print()
#pattern5()

def pattern6():
    for i in range(5,1,-1):
        for j in range(1,i):
            print(j, end=" ")
        print()
#pattern6()

def pattern7():
    n=5
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*",end=" ")
        print()
#pattern7()

def pattern8():
    n=5
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print()
#pattern8()

def pattern9():
    n=5
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print()
#pattern9()

def pattern10():
    for i in range(1, 5):
        for j in range(i):
            print("*", end=" ")
        print()
    for i in range(5,1,-1):
        for j in range(i-1,1,-1):
            print("*", end=" ")
        print()
#pattern10()

def pattern11():
    n=5
    start = 1
    for i in range(1,n+1):
        if i%2==0:
            start=0
        else:
            start=1
        for j in range(i):
            print(start,end=" ")
            start = 1-start
        print()
#pattern11()

def pattern12():
    n = 5
    for i in range(1, n + 1):
        # left
        for j in range(1, i + 1):
            print(j, end="")
        # spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # right
        for j in range(i, 0, -1):
            print(j, end="")
        print()
#pattern12()

def pattern13():
    n=5
    num1=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num1,end=" ")
            num1+=1
        print()
#pattern13()

def pattern14():
    for i in range(6):
        ch = "A"
        for j in range(i):
            print(ch,end=" ")
            ch = chr(ord(ch)+1)
        print()
#pattern14()

def pattern15():
    for i in range(5,0,-1):
        ch = "A"
        for j in range(i):
            print(ch, end=" ")
            ch = chr(ord(ch)+1)
        print()
#pattern15()

def pattern16():
    for i in range(6):
        ch = chr(ord('A')+i-1)
        for j in range(i):
            print(ch,end=" ")
        print()
#pattern16()

def pattern17():
    n = 5
    for i in range(1, n + 1):
        # spaces
        for j in range(n - i):
            print(" ", end=" ")
        # increasing (A → current)
        for j in range(i):
            print(chr(ord('A') + j), end=" ")
        # decreasing (reverse)
        for j in range(i - 2, -1, -1):
            print(chr(ord('A') + j), end=" ")
        print()
#pattern17()

def pattern18():
    n = 5
    for i in range(1, n + 1):
        ch = ord('E')   # start from 'E'
        for j in range(i):
            print(chr(ch), end=" ")
            ch -= 1     # move backward
        print()
#pattern18()

def pattern19():
    n = 5
    # Top part
    for i in range(n):
        # left stars
        for j in range(n - i):
            print("*", end="")
        # middle spaces
        for j in range(2 * i):
            print(" ", end="")
        # right stars
        for j in range(n - i):
            print("*", end="")
        print()
    # Bottom part
    for i in range(n - 2, -1, -1):
        # left stars
        for j in range(n - i):
            print("*", end="")
        # middle spaces
        for j in range(2 * i):
            print(" ", end="")
        # right stars
        for j in range(n - i):
            print("*", end="")    
        print()
#pattern19()

def pattern20():
    n=5
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
#pattern20()

def pattern21():
    n=5
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
#pattern21()

def pattern22():
    n = 4
    size = 2*n - 1
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            minimum = min(top, left, bottom, right)
            val = n - minimum
            print(val, end=" ")
        print()
pattern22()
