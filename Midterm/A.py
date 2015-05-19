num = input()
split = num.split()

if len(split) == 1 and num != 'Ug!' :
    dec = int(num)
    if dec == 1 :
        print('Ug!')
    elif dec > 0 :
        dec -= 1
        output = 'Ug'
        for i in range(0, dec) :
            output += ' ug'
        output += '!'
        print(output)
else :
    print(len(split))
