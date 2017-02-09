#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all(class_="story-heading")[:10]:
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url2 = 'https://www.michigandaily.com/'
r = requests.get(base_url2)
soup = BeautifulSoup(r.text, "html.parser")

for most_read_heading in soup.find_all(class_="view-most-read"):
    a = most_read_heading.find_all('a')
    for a1 in a:
        print(a1.text)

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url2 = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url2)
soup = BeautifulSoup(r.text, "html.parser")

for images in soup.find_all("img"):
    if images.get('alt'):
        print(images.get('alt'))
    else:
        print("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
import re

base_url2 = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'

urllist = []
pagelist = [base_url2]

def find_contact_info():
    for items in soup.find_all(class_="field-item"):
        a = items.find_all('a')
        if a:
            for a1 in a:
                x = re.findall('Contact Details', a1.text)
                if x != []:
                    urllist.append("https://www.si.umich.edu" + a1.get('href'))

def find_next_page():
    for items in soup.find_all(class_="item-list"):
        a = items.find_all('a')
        if a:
            for a1 in a:
                x = re.findall('next', a1.text)
                if x != []:
                    pagelist.append("https://www.si.umich.edu" + a1.get('href'))

for pages in pagelist:
    r = requests.get(pages)
    soup = BeautifulSoup(r.text, "html.parser")
    find_contact_info()
    find_next_page()

n = 0
for url in urllist:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for items in soup.find_all(class_="field-item"):
        a = items.find_all('a')
        if a:
            for a1 in a:
                n += 1
                print(n, a1.text)
            break
