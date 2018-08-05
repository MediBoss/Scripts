def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for data in range(0,3):
        if not isInstance(data, Int):
            return False
    if text[3] != '-':
        return False

    for data in range(4,7):
        if is not isInstance(data, Int):
            return false
    if text[7] != '-':
        return False



def main():

    print(isPhoneNumber('Is 862-321-7478 is a phone number'))
    print(isPhoneNumber('Is 12-321-7478 is a phone number'))
    print(isPhoneNumber('Is mashak is a phone number'))
    print(isPhoneNumber('Is 654-7897-8765 is a phone number'))


if __name__ == '__main__':
    main()
