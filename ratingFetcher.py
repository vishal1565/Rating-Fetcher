import sys
from codechefRating import *
from cfRating import *

def printUse():
    print("Usage: python ratingFetcher.py -cc [codechef-username] -cf [codeforces-username]")
# Checking input Format
try:
    if len(sys.argv)==3:
        if sys.argv[1]=='-cc':
            getRating(sys.argv[2])
        elif sys.argv[1]=='-cf':
            cfRating(sys.argv[2])
        else:
            printUse()
    elif len(sys.argv)==5:
        if sys.argv[1]=='-cc':
            getRating(sys.argv[2])
        elif sys.argv[1]=='-cf':
            cfRating(sys.argv[2])
        else:
            printUse()
        if sys.argv[3]=='-cc':
            getRating(sys.argv[4])
        elif sys.argv[3]=='-cf':
            cfRating(sys.argv[4])
        else:
            printUse()
    else:
        printUse()
except:
    pass