def match(words, possibleWords, word) :
    matches = []
    word = removeDuplicates(word)
    for i in range(0, len(possibleWords)) :
        match = possibleWords[i]
        if match[0] != word[0] or match[len(match) - 1] != word[len(word) - 1] :
            continue
        pointer = 1
        if word == match :
            print(words[i])
            return
        for j in range(1, len(word)) :
            if pointer < len(match) and match[pointer] == word[j] :
                pointer += 1
            if pointer == len(match) :
                print(words[i])
                return
    print('?')

def removeDuplicates(word) :
    newWord = word[0]
    for i in range(1, len(word)) :
        if word[i-1] != word[i] :
            newWord += word[i]
    return newWord

k = int(input())
words = []

for i in range(0, k) :
    words.append(input())

n = int(input())
inputlist = []

for i in range(0, n) :
    inputlist.append(input())

possibleWords = []
for i in range(0, len(words)) :
    word = words[i][0]
    for j in range(1, len(words[i])) :
        if words[i][j-1] != words[i][j] :
            word += words[i][j]
    possibleWords.append(word)

for i in range(0, len(inputlist)) :
    match(words, possibleWords, inputlist[i])
