#Count number of words in a file
def count_words():
    with open("sample.txt", "r") as f:
        data = f.read()
        words = data.split()   # split by spaces
        print("Number of words:", len(words))

count_words()

#Count number of lines in a file
def count_lines():
    count = 0

    with open("sample.txt", "r") as f:
        for line in f:
            count += 1

    print("Number of lines:", count)

count_lines()

#search for a word
def search_word():
    word = "Amazon"

    with open("sample.txt", "r") as f:
        data = f.read()

        if word in data:
            print("Word found")
        else:
            print("Word not found")

#search_word()

#Count how many times a word appears
def count_word():
    word = "Amazon"
    count = 0

    with open("sample.txt", "r") as f:
        data = f.read().lower()
        words = data.split()

        for w in words:
            if w == word.lower():
                count += 1

    print("Word count:", count)

count_word()