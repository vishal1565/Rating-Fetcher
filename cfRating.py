import requests
from bs4 import BeautifulSoup as bs
import re

tagRe = re.compile(r'<[^>]+>')

def removeTags(text):
    return tagRe.sub('',text)

def cfRating(username):
    print("Fetching Codeforces Profile....")
    profile = 'https://codeforces.com/profile/'+username
    req = requests.get(profile)
    soup = bs(req.text,'html.parser')
    temp = soup.find_all('span',class_='user-gray')
    rating = removeTags(str(temp[-1]))
    currTitle = removeTags(str(temp[0]))
    temp = soup.find_all('span',class_='user-green')
    maxRating = removeTags(str(temp[-1]))
    maxTitle = removeTags(str(temp[-2])).replace(',','')
    print()
    print("+--------------------+")
    print("| CodeForces Profile |")
    print("+--------------------+")
    print("Profile Link :",profile)
    print("UserName :",username)
    print("Current Rating :",rating)
    print("Max Rating :",maxRating)
    print("Current Title :",currTitle)
    print("Highest Title :",maxTitle)
#cfRating('yamraj_1565')