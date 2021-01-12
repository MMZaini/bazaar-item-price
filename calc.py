from bs4 import BeautifulSoup
import time
import requests
import asyncio
item = input("What Item Would You Like To Check The Price Of?\n")
page = requests.get("https://stonks.gg/products/search?input=" + item)
soup = BeautifulSoup(page.content, 'html.parser')
bfa = soup.find(class_="table table-striped table-sm text-right")
fbfa = bfa.find_all("tr")

"""
for i, x in enumerate(fbfa[:5]):
    print(i, x)
"""

"""
1. input amount to spend named amount
2. amount / price and print answer
"""

price = float(fbfa[1].find_all("td")[2].text.split(" ")[0]) + 0.5
print("Buy price is currently", price, "per", item)
time.sleep(1.5)
amount = float(input("How much would you like to spend?\n"))
amo = amount // price
s = "s"
if amo > 1:
    print("Purchase", amo, item + s)
if amo == 1:
    print("Purchase", amo, item)
if amo < 1:
    print("You don't have enough to buy any", item + s)

loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()
