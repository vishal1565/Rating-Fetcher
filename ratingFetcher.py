import sys
from codechefRating import *

# Checking input Format
try:
    if len(sys.argv)!=2:
        print("Usage: python ratingFetcher.py [username]")
    else:
        print("Fetching Rating")
        getRating(sys.argv[-1])
except:
    pass