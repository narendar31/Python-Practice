text='hello welcome to python strings'
words=text.split(" ")#for split the words
for i in text:#for each letter will be print
    print(i)
    print("_________________")
    for word in words:
     print(word)
print(len(words))
print(len(text))