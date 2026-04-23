#Find largest and smallest in list
def lar_small_element():
    lst = [1, 2, 3, 4, 5, 6]
    smallest = lst[0]
    largest = lst[0]

    for num in lst:
        if num<smallest:
            smallest = num
        if num>largest:
            largest = num
    print("smallest: ", smallest)
    print("largest: ",largest)
#lar_small_element()

#Find second largest number
def second_largest():
    lst = [1,4,6,7,9,8]
    largest = lst[0]
    second = lst[0]
    for num in lst:
        if num>largest:
            largest = num
    for num in lst:
       if num != largest:
           if second == largest or num>second:
               second = num
    
    print("Second largest: " ,second)
#second_largest()

#Remove duplicates from list
def rmv_duplicates():
    lst = [4, 5, 4, 5, 6, 7]
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    print(result)
#rmv_duplicates()

def count_even_odd():
    lst = [1, 2, 3, 4, 5, 6]

    even = 0
    odd = 0

    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd:", odd)

#count_even_odd()

#Find common elements in two lists
def common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    print(result)

common_elements()



