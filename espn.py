from urllib.request import urlopen
from bs4 import BeautifulSoup
def main():

	print()

	player = "jimmy-butler"

	html = urlopen("http://espn.go.com/nba/player/gamelog/_/id/6430/"+player)
	bsObj = BeautifulSoup(html.read(), "html.parser")
	st1 = (bsObj.findAll("tr", {"class":"oddrow team-46-5"}))
	st2 = (bsObj.findAll("tr", {"class":"evenrow team-46-5"}))

	#found = bsObj.find("tr", { "class" : "oddrow player-46-6430" })
	#print(found)
	#print(found.td)
	#print(found.td)
	#"""

	for i in range(2):
		

		obj = st1[i].findAll("td")
		
		playr = player.split("-")
		print("Player:" , playr[0].capitalize(), playr[1].capitalize())
		print("Date:" , obj[0].getText())
		opp = obj[1].getText()
		print("Opponent:", opp[2:])
		print("Minutes:" ,obj[3].getText())
		x = obj[4].getText().split("-")
		print("Shots Made:" ,x[0])
		print("Shots Attempted:" ,x[1])
		x = obj[6].getText().split("-")
		print("3-Point Shots Made:" ,x[0])
		print("3-Point Shots Attempted:" ,x[1])
		x = obj[8].getText().split("-")
		print("Free Throws Made:" ,x[0])
		print("Free Throws Attempted:" ,x[1])
		print("Rebounds:", obj[10].getText())
		print("Assists:", obj[11].getText())
		print("Blocks:", obj[12].getText())
		print("Steals:", obj[13].getText())
		print("Fouls:", obj[14].getText())
		print("Turnovers:", obj[15].getText())
		print("Points:", obj[16].getText())
		print()

	for i in range(2):
	
		obj = st2[i].findAll("td")
		
		playr = player.split("-")
		print("Player:" , playr[0].capitalize(), playr[1].capitalize())
		print("Date:" , obj[0].getText())
		opp = obj[1].getText()
		print("Opponent:", opp[2:])
		print("Minutes:" ,obj[3].getText())
		x = obj[4].getText().split("-")
		print("Shots Made:" ,x[0])
		print("Shots Attempted:" ,x[1])
		x = obj[6].getText().split("-")
		print("3-Point Shots Made:" ,x[0])
		print("3-Point Shots Attempted:" ,x[1])
		x = obj[8].getText().split("-")
		print("Free Throws Made:" ,x[0])
		print("Free Throws Attempted:" ,x[1])
		print("Rebounds:", obj[10].getText())
		print("Assists:", obj[11].getText())
		print("Blocks:", obj[12].getText())
		print("Steals:", obj[13].getText())
		print("Fouls:", obj[14].getText())
		print("Turnovers:", obj[15].getText())
		print("Points:", obj[16].getText())
		print()


	
main()