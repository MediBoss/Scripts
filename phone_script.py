# Simple script that checks if a data passed as parameter is a phone number or not.

#! usr/bin/env/ python3
def isPhoneNumber(text):

    if len(text) != 12:
        return False
    for data in range(0,3):
        if isinstance(data, int) is False:
            return False
    if text[3] != '-':
        return False
    for data in range(4,7):
        if isinstance(data, int) != True:
            return false
    if text[7] != '-':
        return False
    for data in range(8,12):
        if isinstance(data, int) != True:
            return False
    return True

def main():

    print("Is 456-876-8976 a phone number : {}".format(isPhoneNumber('456-876-8976')))
    print("Is 45-876-8346 a phone number : {}".format(isPhoneNumber('45-876-8346')))
    print("Is 456-87-8972 a phone number : {}".format(isPhoneNumber('456-87-8972')))
    print("Is 862-321-1232 a phone number : {}".format(isPhoneNumber('862-321-1232')))


if __name__ == '__main__':
    main()
