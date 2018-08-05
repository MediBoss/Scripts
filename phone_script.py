
'''
    This script parses through a text file that contains an article. Within the article, there are some
    phone numbers. The job of this script is to recognize and find every single phone number(USA).
    Example : Phone number found : 8623427865
'''

import os

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

def parse():
    try:
        with open('article.txt',r) as file:
            


    except IOError:
        # error


def main():


if __name__ == '__main__':
    main()
