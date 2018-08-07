
'''
    This script parses through a text file that contains an article. Within the article, there are some
    phone numbers. The job of this script is to recognize and find every single phone number.
    Fomrat of typical phone (n) numbers: nnn-nnn-nnn , (nnn) nnn-nnnn, nnn.nnn.nnnn, nnn-nnn-nnnn xnn
'''
#! /usr/bin/env python
import os
import re

# Function to detect if a string passed as a parameter is a phone number
def isPhoneNumber(text):

    first_phone_exp = re.compile(r'(\d{3}-)?\d{3}-\d{4})')# represents the nnn-nnn-nnn cell phone format with the an area code optional
    second_phone_exp = re.compile(r'\d{3}.\d{3}.\d{4}') # represents the nnn.nnn.nnn cell phone format
    third_phone_expx = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # represents the  (nnn) nnn-nnnn cell phone format

        #Checking properties of a standard phone number
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

# Function to parse through the text file
def parse_article():
    file_path = 'article.txt'
    try:
        with open(file_path,'r') as article:
            for current_line in article:
                for index in range(len(current_line)):
                    chunk_of_data = current_line[index:index+12]
                    if isPhoneNumber(chunk_of_data):
                        print('Phone number found : {}'.format(chunk_of_data))

    except IOError:
        print("ERROR FOUND : FILE COULD NOT BE OPENED")

def main():

    parse_article()

if __name__ == '__main__':
    main()
