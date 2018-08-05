#! usr/bin/env/ python3

import sys

PASSWORDS = {'email': 'eroku123',
             'facebook': 'zuckeberg243',
             'instagram': 'xio345'}

if len(sys.argv) < 2:
    print('Usage: Pyhton pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    #pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named '+ account)
