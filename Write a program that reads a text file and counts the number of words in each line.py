#The program should print the line number and the word count for each line, as well as the total number of words in the file.
with open('test.txt','r') as file:
    content= file.readlines()
    total_words=0
    line_count=0
    for line in content:
        line=line.strip()
        words=line.split()
        word_count=len(words)
        total_words+=word_count
        line_count+=1
print('total number of lines:',line_count)
print('total number of words:',total_words)
