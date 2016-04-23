from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

def main():

	'''
	--------- -------- ------- CLEAR TABLES BEFORE RUNNING ------- - ------- --------- 
	'''

	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')

	cur = conn.cursor()

	cur.execute("DELETE FROM Data")
	cur.execute("DELETE FROM Player")
	cur.execute("DELETE FROM Opponents")
	cur.execute("DELETE FROM Games")

	#print()

	'''

	< --------------------- Jimmy Butler --------------------------------------------------------------- >
	< -------------------------------------------------------------------------------------------------- > 
	
	'''


	player_array = ["jimmy-butler", "cameron-bairstow", "aaron-brooks", "mike-dunleavy", "cristiano-felicio", "pau-gasol", "taj-gibson", "justin-holidy", "doug-mcdermott", "nikola-mirotic", "e'twaun-moore", "joakim-noah", "bobby-ports", "derrick-rose", "tony-snell"]

	id_num = 0
	game_id = 0
	oppo_bool = False

	for plyer in range(1,(len(player_array)+1)):

		print("Player: ",player_array[plyer-1],"is done!")

		player = player_array[plyer-1]

		html = urlopen("http://espn.go.com/nba/player/gamelog/_/id/6430/"+player)
		bsObj = BeautifulSoup(html.read(), "html.parser")


		# Age
		s = (bsObj.findAll("ul", {"class":"player-metadata floatleft"}))
		t = s[0].findAll("li")
		j = t[1].findAll("span")
		f = t[0].getText()
		y = len(f) - 1
		x = y - 2
		age = int(f[x:y])

		playr = player.split("-")

		id_num += 1
		first = playr[0].capitalize()
		last = playr[1].capitalize()

		cur.execute('insert into Player values ("%s","%s","%s","%s")' % (id_num,first,last,age))




		'''


		'''
		#< ------------- vs --------------------------------------------------- >
		
		#game_id = 0
		
		for v in range(1,30):

			if (v == 4):
				continue
			else:
				v = str(v)
				st1 = (bsObj.findAll("tr", {"class":"oddrow team-46-"+v}))
				st2 = (bsObj.findAll("tr", {"class":"evenrow team-46-"+v}))

				for i in range(len(st1)):

					game_id += 1
					

					obj = st1[i].findAll("td")
					
					playr = player.split("-")
					#print("Player:" , playr[0].capitalize(), playr[1].capitalize())

					#print("Date:" , obj[0].getText())
					date = obj[0].getText()

					opp = obj[1].getText()
					#print("Opponent 1:", opp[2:])
					opponent = opp[2:]

					#score
					q = obj[2].findAll("a")
					score = q[0].getText()
					#print("Score:",score)

					#print("Minutes:" ,obj[3].getText())
					minu = obj[3].getText()

					x = obj[4].getText().split("-")
					#print("Shots Made:" ,x[0])
					#print("Shots Attempted:" ,x[1])
					fg_made = x[0]
					fg_attempted = x[1]

					x = obj[6].getText().split("-")
					#print("3-Point Shots Made:" ,x[0])
					#print("3-Point Shots Attempted:" ,x[1])
					three_made = x[0]
					three_attempted = x[1]

					x = obj[8].getText().split("-")
					#print("Free Throws Made:" ,x[0])
					#print("Free Throws Attempted:" ,x[1])
					free_made = x[0]
					free_attempted = x[1]

					#print("Rebounds:", obj[10].getText())
					rebounds = obj[10].getText()

					#print("Assists:", obj[11].getText())
					assists = obj[11].getText()

					#print("Blocks:", obj[12].getText())
					blocks = obj[12].getText()

					#print("Steals:", obj[13].getText())
					steals = obj[13].getText()

					#print("Fouls:", obj[14].getText())
					fouls = obj[14].getText()

					#print("Turnovers:", obj[15].getText())
					turnovers = obj[15].getText()

					#print("Points:", obj[16].getText())
					points = obj[16].getText()

					#print()

					if plyer == 1:

						cur.execute('insert into Games values ("%s","%s","%s","%s")' % (game_id, opponent , date, score))

					# not done with this statement
					cur.execute('insert into Data values ("%s","%s","%s","%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s")' % (game_id, game_id ,id_num, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points ))

				for i in range(len(st2)):

					if plyer == 1:
						oppo_bool = True

					game_id += 1
				
					obj = st2[i].findAll("td")
					
					playr = player.split("-")
					#print("Player:" , playr[0].capitalize(), playr[1].capitalize())

					#print("Date:" , obj[0].getText())
					date = obj[0].getText()

					opp = obj[1].getText()
					#print("Opponent:", opp[2:])
					opponent = opp[2:]

					#score
					q = obj[2].findAll("a")
					score = q[0].getText()
					#print("Score:",score)

					#print("Minutes:" ,obj[3].getText())
					minu = obj[3].getText()

					x = obj[4].getText().split("-")
					#print("Shots Made:" ,x[0])
					#print("Shots Attempted:" ,x[1])
					fg_made = x[0]
					fg_attempted = x[1]

					x = obj[6].getText().split("-")
					#print("3-Point Shots Made:" ,x[0])
					#print("3-Point Shots Attempted:" ,x[1])
					three_made = x[0]
					three_attempted = x[1]

					x = obj[8].getText().split("-")
					#print("Free Throws Made:" ,x[0])
					#print("Free Throws Attempted:" ,x[1])
					free_made = x[0]
					free_attempted = x[1]

					#print("Rebounds:", obj[10].getText())
					rebounds = obj[10].getText()

					#print("Assists:", obj[11].getText())
					assists = obj[11].getText()

					#print("Blocks:", obj[12].getText())
					blocks = obj[12].getText()

					#print("Steals:", obj[13].getText())
					steals = obj[13].getText()

					#print("Fouls:", obj[14].getText())
					fouls = obj[14].getText()

					#print("Turnovers:", obj[15].getText())
					turnovers = obj[15].getText()

					#print("Points:", obj[16].getText())
					points = obj[16].getText()

					#print()
					if plyer == 1:
						cur.execute('insert into Games values ("%s","%s","%s","%s")' % (game_id, opponent , date, score))

					#if oppo_bool:
						#cur.execute('insert into Opponents values ("%s","%s")' % (v , opponent))
			#oppo_bool = False

	cur.close()
	conn.commit()
	conn.close()

	
	#< ----------------------------------------------------------------------- >
	#< ------------- vsPHI --------------------------------------------------- >

	'''
	'''

	#< -------------------------------------------------------------------------------------------------- >
	#< -------------------------------------------------------------------------------------------------- > 
	
	'''


	'''

main()