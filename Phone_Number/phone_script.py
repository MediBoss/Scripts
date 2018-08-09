
'''
    This script parses through a text file that contains an article. Within the article, there are some
    phone numbers. The job of this script is to recognize and find every single phone number.
    Fomrat of typical phone (n) numbers: nnn-nnn-nnn , (nnn) nnn-nnnn, nnn.nnn.nnnn, nnn-nnn-nnnn xnn
'''
#! /usr/bin/env python
import os
import re

# Function to detect if a string passed as a parameter is a phone number
def isPhoneNumber(data):

    #first_phone_exp = re.compile(r'(\d{3}-)?\d{3}-\d{4}')# represents the nnn-nnn-nnn cell phone format with the an area code optional
    #second_phone_exp = re.compile(r'\d{3}.\d{3}.\d{4}') # represents the nnn.nnn.nnn cell phone format
    #third_phone_expx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # represents the  (nnn) nnn-nnnn cell phone format
    results = []
    phone_exp = re.compile(r'\d{3}-\d{3}-\d{4}|\d{3}.\d{3}.\d{4}')
    return results.append(phone_exp.findall(data))

# Function to parse through the text file
def parse_article():
    file_path = 'article.txt'
    try:
        with open(file_path,'r') as article:
            for current_line in article:
                isPhoneNumber(line)

    except IOError:
        print("ERROR FOUND : FILE COULD NOT BE OPENED")

def main():

    parse_article()

if __name__ == '__main__':
    main()
