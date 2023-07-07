
word_count = {}

with open('test.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

print(word_count)
