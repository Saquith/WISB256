hoogste = int(input())
lst = list(input())
standing = 0
friends = 0

for i in range(0, len(lst)) :
    amount = int(lst[i])
    if standing + friends >= min(i, hoogste) :
        standing += amount
    else :
        friends += i - (standing + friends)
        standing += amount

print(friends)
