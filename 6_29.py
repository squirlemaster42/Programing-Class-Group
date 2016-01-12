def isValid(number):
    if getSize(number) >= 13 and getSize(number) <= 16 and (prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 6) or prefixMatched(number, 37)) and (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
        return True
    else:
        return False

def getSize(d):
    count = 0
    while d > 0:
        count += 1
        d = d//10

    return count

def getDigit(number):
    isSingle = 0
    while isSingle != 1:
        if number // 10 == 0:
            isSingle = 1
        else:
            number = number // 10 + number % 10
    return number

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

def sumOfOddPlace(number):
    total = 0
    size = getSize(number)
    while number > 0:
        total += number % 10
        number = number // 100
    return total

def sumOfDoubleEvenPlace(number):
    number = number // 10
    total = 0
    size = getSize(number)
    while number > 0:
        num = (number % 10) * 2
        if num <= 10:
            temp1 = num // 10
            temp2 = num % 10
            num = temp1 + temp2
            total += num
        else:
            total += num
        number = number // 100
    return total

def prefixMatched(number, d):
    if getPrefix(number, getSize(d)) == d:
        return True
    else:
        return False

def main():
    creditCard = eval(input("Enter a credit card number to be tested here: "))
    if isValid(creditCard):
        print("That credit card is valid.")
    else:
        print("That credit card is invalid.")

main()
