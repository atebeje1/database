# source 1

# import library that allows us to pull data from websites
import requests

# requests data from url below
request = requests.get('https://www.adl.org/hate-symbols')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content)

# filters soup to only display what is specified
specificData = soup.find_all('img')

# finds and prints alternative text for images at above url
for x in specificData:
  print(x['alt'])

# source 2

# requests data from url below
request = requests.get('https://archive.attn.com/stories/7307/common-expressions-words-that-are-sexist')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content)

# filters soup to only display what is specified
specificData = soup.find_all('h2')

# finds and prints text from chart at above url
count = 1
resultArray = []
for z in specificData:
  result = z.find(text=True)[3:]
  if "/" in result:
    resultArray = result.split("/")
    print(resultArray[0])
    print(resultArray[1])
    count = count + 1
  elif count < 7:
   count = count +1
   print(result)
