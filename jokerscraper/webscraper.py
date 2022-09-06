import random
import requests
import asyncio
from bs4 import BeautifulSoup


listOfQuotes = []

def initSleepy():
    print("RELEASING SLEEPY JOKER!!!!!!!!!!!!!!")
    asyncio.sleep(random.randint(6,9))
    pickRandomQuote()

def retrieveData(urlToParse):
    reqList = requests.get(urlToParse)
    return reqList.text

def initializeList(data):
    listOfQuotes.append(data)

def pickRandomQuote():
    return random.choice(listOfQuotes) + "FUCK"

# Retrieving data source & initializing url
url = "https://parade.com/1231125/jessicasager/joker-quotes/"


#Initializing beautiful soup object
soup = BeautifulSoup(retrieveData(url), 'lxml')

#Pulling & parsing
i = 0
for x in soup.find_all("p"):
    try:
        if(str(str(x.get_text())[0]).isdigit()):
            initializeList(x.get_text())
    except:
        print("THIS MOTHERFUCKER BROKE")


print(pickRandomQuote())

