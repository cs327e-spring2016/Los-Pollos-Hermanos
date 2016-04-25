from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

def main():

	print("Starting to scrape...")
	print('...')

	'''
	--------- -------- ------- CLEAR TABLES BEFORE RUNNING ------- - ------- --------- 
	'''

	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')

	cur = conn.cursor()

	cur.execute("DELETE FROM Data")
	cur.execute("DELETE FROM Player")
	cur.execute("DELETE FROM Opponents")
	cur.execute("DELETE FROM Games")


	player_array = ["jimmy-butler", "cameron-bairstow", "aaron-brooks", "mike-dunleavy", "cristiano-felicio", "pau-gasol", "taj-gibson", "justin-holidy", "doug-mcdermott", "nikola-mirotic", "e'twaun-moore", "joakim-noah", "bobby-ports", "derrick-rose", "tony-snell"]

	id_num = 0
	game_id = 0
	oppo_bool = False


	for plyer in range(1,(len(player_array)+1)):

		ayer = player_array[plyer-1]
		ayer = ayer.split("-")

		print("Player: ", ayer[0].capitalize(), ayer[1].capitalize(),"is starting!")

		player = player_array[plyer-1]

		html = urlopen("http://espn.go.com/nba/player/gamelog/_/id/6430/"+player)
		bsObj = BeautifulSoup(html.read(), "html.parser")


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

					date = obj[0].getText()

					opp = obj[1].getText()
					opponent = opp[2:]

					q = obj[2].findAll("a")
					score = q[0].getText()

					minu = obj[3].getText()

					x = obj[4].getText().split("-")
					fg_made = x[0]
					fg_attempted = x[1]

					x = obj[6].getText().split("-")
					three_made = x[0]
					three_attempted = x[1]

					x = obj[8].getText().split("-")
					free_made = x[0]
					free_attempted = x[1]

					rebounds = obj[10].getText()

					assists = obj[11].getText()

					blocks = obj[12].getText()

					steals = obj[13].getText()

					fouls = obj[14].getText()

					turnovers = obj[15].getText()

					points = obj[16].getText()

					if plyer == 1:

						cur.execute('insert into Games values ("%s","%s","%s","%s")' % (game_id, opponent , date, score))

					cur.execute('insert into Data values ("%s","%s","%s","%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s")' % (game_id, game_id ,id_num, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points ))

				for i in range(len(st2)):

					if plyer == 1:
						oppo_bool = True

					game_id += 1
				
					obj = st2[i].findAll("td")
					
					playr = player.split("-")

					date = obj[0].getText()

					opp = obj[1].getText()
					opponent = opp[2:]

					q = obj[2].findAll("a")
					score = q[0].getText()

					minu = obj[3].getText()

					x = obj[4].getText().split("-")
					fg_made = x[0]
					fg_attempted = x[1]

					x = obj[6].getText().split("-")
					three_made = x[0]
					three_attempted = x[1]

					x = obj[8].getText().split("-")
					free_made = x[0]
					free_attempted = x[1]

					rebounds = obj[10].getText()

					assists = obj[11].getText()

					blocks = obj[12].getText()

					steals = obj[13].getText()

					fouls = obj[14].getText()

					turnovers = obj[15].getText()

					points = obj[16].getText()

					if plyer == 1:
						cur.execute('insert into Games values ("%s","%s","%s","%s")' % (game_id, opponent , date, score))

		print("Player: ", ayer[0].capitalize(), ayer[1].capitalize(),"is done!")

	print()
	start = input("Ready to start querying?(yes/no) ")

	if start.lower() != "yes":
		print("BYE!")
		return

	print("GREAT!")
	print()

	c = True

	while c == True:
		print("Tables: Player, Data, Games")
		print()
		table = input("What table would you like to query? ")
		print("Thanks!")
		print()

		if (table.lower() == "player"):
			print("Table", table.capitalize(), "has: id_pk , fist , last ,and age for each player")
			print()
			select = input("What would you like to select(use commas to separate values)? ")
			select2 = select.split(",")
			print(select)
			c = False
		elif (table.lower() == "data"):
			print("Table", table.capitalize(), "has: id_pk , game_fk , player_fk , minutes  , fg_made , fg_attempted , three_made , three_attempted , free_made , free_attempted , rebounds , assists , blocks , steals , fouls , turnovers ,  points for each Player in each Game played")
			print()
			select = input("What would you like to select(use commas to separate values)? ")
			select2 = select.split(",")
			print(select)
			c = False
		elif (table.lower() == "games"):
			print("Table", table.capitalize(), "has: id_pk , opponent , date , and score for each game")
			print()
			select = input("What would you like to select(use commas to separate values)? ")
			select2 = select.split(",")
			print(select)
			c = False
		else:
			print("Seems like your spelling may be incorrect, lets try again.")
			c = True


	print("What conditions would you like to add(ex first = 'jimmy', age >= 20)?")
	print()
	whre = input("WHERE: ")

	print()

	print("Is this the query you'd like to run?")
	print()
	table = table.capitalize()
	print("SELECT", select, "FROM",table, "WHERE", whre)
	print()
	statement = input("(yes/no): ")
	print()
	if (statement.lower() == "yes"):
		hfg = cur.execute('SELECT %s FROM %s WHERE %s' % (select, table, whre))
		p = cur.fetchall()
		for row in p:
			print(row)


	cur.close()
	conn.commit()
	conn.close()

main()