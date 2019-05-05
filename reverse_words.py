def reverseWords(s):
    wordList = s.split(" ")
    revWordList = wordList[::-1] 
    newWordList = []
    for w in revWordList:
        revWord = w[::-1]
        newWordList.append(revWord)
    return " ".join(newWordList)

line = "geeks quiz practice code"
print(reverseWords(line))


