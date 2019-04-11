from bs4 import BeautifulSoup as bs
import requests
import sys
import re

tagRe = re.compile(r'<[^>]+>')

def removeTags(text):
    return tagRe.sub('',text)

def getRating(username):
    profileLink = 'https://www.codechef.com/users/'+username
    #print("\nCodeChef Profile Url: "+profileLink)
    try:
        page = requests.get(profileLink)
        soup = bs(page.text, 'html.parser')

        rating = soup.find_all('div',class_='rating-container')
        temp = rating[0].a.text.split()
        name = soup.find_all('h2')
        name = removeTags(str(name[-1]))
        institute = soup.find_all('ul',class_='side-nav')
        institute = str(bs(institute[0].text,'html.parser')).split('\n')
        for i in institute:
            if 'Institution' in i:
                res = i
                break
        print()
        print("+------------------+")
        print("| CodeChef Profile |")
        print("+------------------+")
        print("Profile Link:",profileLink)
        print("Coder Name:",name)
        print("Rating of",username+":", temp[0])
        print(res.replace(':',": "))
    except:
        print("An error Occurred!!")

#getRating(input())