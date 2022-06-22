import mechanicalsoup

import requests
from bs4 import BeautifulSoup

import json2table
import json

team = "shred"
URL = "https://audl-stat-server.herokuapp.com/web-api/player-stats?limit=22&team=" + team

import requests
r = requests.get(url=URL)
data = json.loads(r.text)
data = json.dumps(data)
parsed = json.loads(data)

name="name"
js = json.loads(r.text)
stats = js['stats']

top_total_yards = []
low_total_yards = []
low_cp = []
high_cp = []
high_recv = []
low_recv = []
low_throwing = []
high_throwing = []

for i in stats:
	if "Selfridge" in i[name]:
		stats.remove(i)
metrics = [ "yardsTotal", "yardsThrown", "yardsReceived", "completionPercentage" ]

# now update for this per game
gamesPlayed="gamesPlayed"

for m in metrics:
	for player in stats:
		games_adjusted_value = float(player[m]) / float(player[gamesPlayed])
		player[m] = games_adjusted_value

def report(stats, key):
	stats.sort(key=lambda x: x[key])
	print ("bottom 10 for: ", key)
	for i in stats[0:7]:
		print("Name:", i[name], str(key),":", i[key], "\n")
		if key == "yardsTotal":
			low_total_yards.append(i)
		if key == "yardsThrown":
			low_throwing.append(i)
		if key == "yardsReceived":
			low_recv.append(i)
		if key == "completionPercentage":
			low_cp.append(i)


	print("top 5 for :", key)
	for i in stats[-5:]:
		print("Name:", i[name], str(key),":", i[key], "\n")
		if key == "yardsTotal":
			top_total_yards.append(i)
		if key == "yardsThrown":
			high_throwing.append(i)
		if key == "yardsReceived":
			high_recv.append(i)
		if key == "completionPercentage":
			high_cp.append(i)




for i in metrics:
	report(stats, i)



stats.sort(key=lambda x: x["completionPercentage"])
print("completionPercentage > 96%")
for i in stats:
	if i["completionPercentage"] > 95.99:
		print("Name:", i[name], "completionPercentage:", i["completionPercentage"], "\n")

print("completionPercentage < 95%")
for i in stats:
	if i["completionPercentage"] < 95.00:
		print("Name:", i[name], "completionPercentage:", i["completionPercentage"], "\n")


print("make them beat us")
for i in stats:
	if i in high_recv and i in low_throwing:
		print("Name:", i[name], "\n")
