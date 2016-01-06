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
    if getPrefix(number, getSize(d)) == d:
        True
    else:
        False

def getSize(d):
    return len(str(d))

def getPrefix(number, k):
    if getSize(number) <= k:
        return number
    else:
        prefix = 0
        i = getSize(number)
        prefix += number // 10 ** (i - 1) * 10 ** (k - 1)
        k -= 1
        i -= 1
        while k > 0:
            prefix += ((number // 10 ** (i - 1)) % 10) * 10 ** (k - 1)
            k -= 1
            i -= 1
        return prefix

def main():
    print("main")

main()
