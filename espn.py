from urllib.request import urlopen
from bs4 import BeautifulSoup
def main():

	player = "jimmy-butler"

	html = urlopen("http://espn.go.com/nba/player/gamelog/_/id/6430/"+player)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	obj = (bsObj.find("tr", {"class":"oddrow team-46-5"}).findAll("td"))
	'''
	'''
	#found = bsObj.find("tr", { "class" : "oddrow player-46-6430" })
	#print(found)
	#print(found.td)
	#print(found.td)
	print("Player: " , player)
	print("Date: " , obj[0].getText())
	print("Minutes: " ,obj[3].getText())
	x = obj[4].getText().split("-")
	print("Shots Made: " ,x[0])
	print("Shots Attempted: " ,x[1])

	
main()