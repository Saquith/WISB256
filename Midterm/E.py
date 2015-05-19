def isOperator(s) :
    return s == '+' or s == '-' or s == '*' or s == '/'

def calc(op, x, y) :
    result = {
          '+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x / y
        }
    return result[op](x, y)

lines = input().split()

while len(lines) > 1 :
    newLines = []
    for i in range(0, len(lines)) :
        if len(lines) == 3 :
            newLines = [calc(lines[2], float(lines[0]), float(lines[1]))]
            break
        elif i + 2 < len(lines) and isOperator(lines[i + 2]) and not isOperator(lines[i + 1]) and not isOperator(lines[i]) :
            newLines.append(calc(lines[i + 2], float(lines[i]), float(lines[i + 1])))
            i += 3
            for j in range(i, len(lines)) :
                newLines.append(lines[j])
            break
        else :
            newLines.append(lines[i])
    lines = newLines

print("{0:.3f}".format(lines[0]))
