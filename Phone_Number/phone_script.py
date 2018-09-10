
'''
    This script parses through a text file that contains an article. Within the article, there are some
    phone numbers. The job of this script is to recognize and find every single phone number.
    Format of typical phone (n) numbers: nnn-nnn-nnn , (nnn) nnn-nnnn, nnn.nnn.nnnn, nnn-nnn-nnnn xnn
'''
#! /usr/bin/env python
import os
import re

# Function to detect if a string passed as a parameter is a phone number
def isPhoneNumber(data):
    first_exp = re.compile(r'\d{3}-\d{3}-\d{4}| \d{3}.\d{3}.\d{4}| \d{3}-\d{4}')
    return first_exp.findall(data)

# Function to parse through the text file
def parse_article():
    file_path = 'article.txt'
    try:
        with open(file_path,'r') as article:
            for current_line in article:
                if len(current_line) != 0:
                    print(isPhoneNumber(current_line))


    except IOError:
        print("ERROR FOUND : FILE COULD NOT BE OPENED")

def main():

    parse_article()

if __name__ == '__main__':
    main()
