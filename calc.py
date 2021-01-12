from bs4 import BeautifulSoup
import requests
item = input("What item would you like\n")
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
amount = float(input("How much would you like to invest?\n"))
amo = amount // price
s = "s"
if amo > 1:
    print("Purchase", amo, item + s)
if amo == 1:
    print("Purchase", amo, item)
if amo < 1:
    print("You don't have enough")
