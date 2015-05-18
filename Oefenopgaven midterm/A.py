def handleInput(sentence) :
    if len(sentence.split()) > 4 :
        print("Crackers!")
        return
    print('%s krAh!' % sentence)

count = int(input())

for i in range(0, count) :
    sentence = input()
    handleInput(sentence)
