import bs4
import requests #this download the actual content
#####To Work around the encoding issue in atom##########
#It looks like atom-script on Windows uses cp1252 (Windows 1252) encoding by default instead of utf-8.


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
####################################################
def getFlipkartPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status() #check for any Exception
#now we use bs4 module and function beautifulSoup
#use html parser or it will prompt for Warning
    soup = bs4.BeautifulSoup(res.text, "html.parser")
# we will use CSS selector to get the price for a product present in above URL
#save the below element to elems
    elems = soup.select("#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1")
#use elems[0].text.strip() to get rid of unnecessary space, tabs and newline
    return elems[0].text

price = getFlipkartPrice('https://www.flipkart.com/nova-supergroom-ng-1149-usb-runtime-60-min-trimmer-men/p/itmaf7717f2800b6?pid=TMRFJ4A5VG72SJFN&lid=LSTTMRFJ4A5VG72SJFNHWW6CH&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3ATMRFJPH3DBURGEZR%3Bl%3ALSTTMRFJPH3DBURGEZRTPHPDK%3Bpt%3App%3Buid%3A047b4da8-86bd-a0ba-27d5-924ec04baf19%3B.TMRFJ4A5VG72SJFN.LSTTMRFJ4A5VG72SJFNHWW6CH&ppt=pp&ppn=pp&ssid=7gh3ih5dkw0000001588352716882&otracker=pp_reco_Similar%2BProducts_2_33.productCard.PMU_HORIZONTAL_Similar%2BProducts_TMRFJ4A5VG72SJFN.LSTTMRFJ4A5VG72SJFNHWW6CH_productRecommendation%2Fsimilar_1&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_2_NA_view-all&cid=TMRFJ4A5VG72SJFN.LSTTMRFJ4A5VG72SJFNHWW6CH')
print('The Price is ' + price)
