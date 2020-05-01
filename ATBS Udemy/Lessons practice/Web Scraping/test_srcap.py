import bs4
import requests #this download the actual content

#def getFlipkartPrice(productURL):
res = requests.get('https://www.flipkart.com/mi-xxq01hm-runtime-90-min-trimmer-men/p/itm97cba5cc90e84?pid=TMRFJPH3DBURGEZR&lid=LSTTMRFJPH3DBURGEZRTPHPDK&marketplace=FLIPKART&spotlightTagId=BestsellerId_zlw%2F79s%2Fby3&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=a3487d88-0256-4534-82f0-ab4ba9df7946.TMRFJPH3DBURGEZR.SEARCH&ppt=sp&ppn=sp&ssid=7gh3ih5dkw0000001588352716882&qH=705a17deac7a99db')
res.raise_for_status() #check for any Exception

#now we use bs4 module and function beautifulSoup

#use html parser or it will prompt for Warning

soup = bs4.BeautifulSoup(res.text, "html.parser")

# we will use CSS selector to get the price for a product present in above URL
#save the below element to elems

elems = soup.select("#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1")

#use elems[0].text.strip() to get rid of unnecessary space, tabs and newline
#print(type(elems[0].text.strip()))
print(elems[0].text)

#print(elems[0].text)

    #return elems[0].text.strip()

#price = getFlipkartPrice('https://www.flipkart.com/mi-xxq01hm-runtime-90-min-trimmer-men/p/itm97cba5cc90e84?pid=TMRFJPH3DBURGEZR&lid=LSTTMRFJPH3DBURGEZRTPHPDK&marketplace=FLIPKART&spotlightTagId=BestsellerId_zlw%2F79s%2Fby3&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=a3487d88-0256-4534-82f0-ab4ba9df7946.TMRFJPH3DBURGEZR.SEARCH&ppt=sp&ppn=sp&ssid=7gh3ih5dkw0000001588352716882&qH=705a17deac7a99db')

#print('The Price is ' + price)
