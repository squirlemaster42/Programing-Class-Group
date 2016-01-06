def isValid(number):
    print("isValid")

def sumOfDoubleEvenPlace(number):
    total = 0
    numString = str(number)
    size = getSize(number)

    for i in range(0, size, 2):
        num = int(numString[i])
        editNum = getDigit(num * 2)
        total += editNum

    return total    

def getDigit(number):
    isSingle = 0
    while isSingle != 1:
        if number // 10 == 0:
            isSingle = 1
        else:
            number = number // 10 + number % 10
    return number

def sumOfOddPlace(number):
    total = 0
    numString = str(number)
    size = getSize(number)

    for i in range(1, size, 2):
        num = int(numString[i])
        total += num

    return total 

def prefixMatched(number, d):
    numString = str(number)
    twoNumString = numString[0] + numString[1]

    if int(numString[0]) == 4:
        value = 4
    elif int(numString[0]) == 5:
        value = 5
    elif int(numString[0]) == 6:
        value = 6
    elif int(twoNumString) == 37:
        value = 37
    else:
        value = 0

    if value == d:
        return True
    else:
        return False

def getSize(d):
    return len(str(d))

def getPrefix(number, k):
    prefix = 0
    i = getSize(number)
    while k > 0:
        prefix += (number // (10 ** (i - 1))) * 10 ** (k - 1)
        k -= 1
    return prefix

def main():
    print("main")

main()
