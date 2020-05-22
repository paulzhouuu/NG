
import bs4
import re
import time
import requests
import csv
pagedata = requests.get(
    "https://www.eia.gov/naturalgas/weekly/archivenew_ngwu/2020/05_14/#tabs-supply-2")

soup = bs4.BeautifulSoup(pagedata.text)
demandTable = soup.findAll("div", {"id": "tabs-supply-2"})
# print(demandTable)
usConsumption = soup.find("td", text="U.S. consumption")
usConsumptionByWeeks = usConsumption.find_next_siblings()
output_row = []
for usConsumptionByWeek in usConsumptionByWeeks:
    div = usConsumptionByWeek.find('div')
    output_row.append(div.text)
    print(div.text)

with open('demand.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(output_row)
