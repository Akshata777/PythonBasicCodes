#Count frequency of elements in a list using dictionary
def frequency():
    lst = [1, 2, 2, 3, 1, 4, 2]
    freq = {}

    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    print(freq)

#frequency()

#Merge two dictionaries
def merge_dict():
    d1 = {1: 'a', 2: 'b'}
    d2 = {3: 'c', 4: 'd'}

    result = {}

    for key in d1:
        result[key] = d1[key]

    for key in d2:
        result[key] = d2[key]

    print(result)

#merge_dict()

#Find key with maximum value
def max_key():
    d = {'a': 10, 'b': 25, 'c': 15}

    max_key = None
    max_value = None

    for key in d:
        if max_value is None or d[key] > max_value:
            max_value = d[key]
            max_key = key

    print("Key with max value:", max_key)

max_key()