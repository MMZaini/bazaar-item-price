#modules - import

from bs4 import BeautifulSoup
import time
import requests

#find website source for item

item = input("What Item Would You Like To Check The Price Of?\n")
page = requests.get("https://stonks.gg/products/search?input=" + item)
soup = BeautifulSoup(page.content, 'html.parser')
bfa = soup.find(class_="table table-striped table-sm text-right")
fbfa = bfa.find_all("tr")

"""
for i, x in enumerate(fbfa[:5]):
    print(i, x)
    
1. input amount to spend named amount
2. amount / price and print answer
"""

#print prices and amount to spend

price = float(fbfa[1].find_all("td")[2].text.split(" ")[0]) + 0.2
print("Buy price is currently", float(price), "per", item)
time.sleep(1)
amount = float(input("How much would you like to spend?\n"))
amo = amount // price
s = "s"
if amo > 1:
    print("Purchase", amo, item + s)
if amo == 1:
    print("Purchase", amo, item)
if amo < 1:
    print("You don't have enough to buy any", item + s)

time.sleep(2)

#license
lic = input("Would you like a copy of this programs license? y or n")
if lic == "y":
 print("Bazaar Calculator  Copyright (C) 2021  Mahdi Zaini This program comes with ABSOLUTELY NO WARRANTY; for details check LICENSE in included download folder. This is free software, and you are welcome to redistribute it under certain conditions; Also check LICENSE included in download folder for details on conditions.")
else:
  input("Press enter 3x to exit program")
  input("Press enter 2x to exit program")
  input("Press enter 1x to exit program")
