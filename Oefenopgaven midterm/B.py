lines = input().split()

firstNumber = int(lines[0])
secondNumber = int(lines[1])
operator = lines[2]

result = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  '/': lambda x, y: x / y
}[operator](firstNumber, secondNumber)

print("{0:.3f}".format(result))
