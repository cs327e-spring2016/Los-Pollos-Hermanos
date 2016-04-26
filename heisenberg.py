from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql



def dbase_init():
	# database connection: add your own passwd
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')
	cur = conn.cursor()


	# tables wiped 
	cur.execute("DELETE FROM Data")
	cur.execute("DELETE FROM Player")
	cur.execute("DELETE FROM Opponents")
	cur.execute("DELETE FROM Games")

	return cur, conn


def scrape(player_array, cur):
	id_num = 0
	game_id = 0
	oppo_bool = False
	data_id = 0
	# iterate over roster
	for plyer in range(1,(len(player_array)+1)):

		game_id = 0


		ayer = player_array[plyer-1]
		ayer = ayer.split("-")

		print("Player: ", ayer[0].capitalize(), ayer[1].capitalize(),"is starting!")

		player = player_array[plyer-1]

		# scrape begins
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

		cur.execute('insert into Player values ("%s","%s","%s","%s")' % (plyer,first,last,age))		

		# iterate over nba teams
		for v in range(1,30):
			# all but chicago bulls
			if (v == 4):
				continue
			else:
				#game_id += 1
				v = str(v)
				st1 = (bsObj.findAll("tr", {"class":"oddrow team-46-"+v}))
				st2 = (bsObj.findAll("tr", {"class":"evenrow team-46-"+v}))

				for i in range(len(st1)):

					game_id += 1
					data_id += 1
					

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

					# only need one data instance of each game
					if plyer == 1:
						#game_id += 1
						#print("tst")
						cur.execute('insert into Games values (%s,"%s","%s","%s")' % (game_id, opponent , date, score))
					# data injection per player and game
					#print(game_id)
					cur.execute('insert into Data values ("%s",%s,%s,"%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s")' % (data_id, game_id ,plyer, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points ))
				# same as above, separation due to html structure
				for i in range(len(st2)):
					data_id += 1
					game_id += 1

					if plyer == 1:
						oppo_bool = True

					#game_id += 1
				
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
						#game_id += 1
						cur.execute('insert into Games values ("%s","%s","%s","%s")' % (game_id, opponent , date, score))
					#print(game_id, "-")
					cur.execute('insert into Data values ("%s",%s,%s,"%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s")' % (data_id, game_id ,plyer, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points ))


		print("Player: ", ayer[0].capitalize(), ayer[1].capitalize(),"is done!")
		# end of scrape




def query_interface (cur, conn):
	# custom query interface
	start = input("Ready to start querying?(yes/no) ")

	if start.lower() != "yes":
		print("BYE!")
		cur.close()
		conn.commit()
		conn.close()
		stop = True
		return stop

	print("GREAT!")
	print()

	c = True
	# iterate until correct table name is specified
	while c == True:
		print("Tables: Player, Data, Games")
		print()
		table = input("What table would you like to query? ")
		print("Thanks!")
		print()

		if (table.lower() == "player"):
			print("Table", table.capitalize(), "has: id_pk , first , last ,and age for each player")
			print()
			# user inputs what columns they'd like to see
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
			print("Table", table.capitalize(), "has: id_pk , opponent_fk , date , and score for each game")
			print()
			select = input("What would you like to select(use commas to separate values)? ")
			select2 = select.split(",")
			print(select)
			c = False
		else:
			print("Seems like your spelling may be incorrect, lets try again.")
			c = True

	# user input WHERE clause
	print("What conditions would you like to add(ex first = 'jimmy', age >= 20)?")
	print()
	whre = input("WHERE: ")

	print()

	# user validation of custom query
	print("Is this the query you'd like to run?")
	print()
	table = table.capitalize()
	print("SELECT", select, "FROM",table, "WHERE", whre)
	print()
	statement = input("(yes/no): ")
	print()
	# sql query construction and output
	if (statement.lower() == "yes"):
		hfg = cur.execute('SELECT %s FROM %s WHERE %s' % (select, table, whre))
		p = cur.fetchall()
		for row in p:
			print(row)


def some_or_all ():

	player_array = ["jimmy-butler", "cameron-bairstow", "aaron-brooks", "mike-dunleavy", "cristiano-felicio", "pau-gasol", "taj-gibson", "justin-holidy", "doug-mcdermott", "nikola-mirotic", "e'twaun-moore", "joakim-noah", "bobby-ports", "derrick-rose", "tony-snell"]
	else_arry_ver = input("Would you like to input all payers or custom select players to import(all/some)? ")
	if else_arry_ver.lower().replace(" ", "") == "some":
		print()
		new_array = input("Type the names of the players youd like to import separated by a comma. (ex jimmy butler , aaron brooks) ")
		new_array = new_array.replace(", ", ",")
		new_array = new_array.replace(" ,", ",")
		new_array = new_array.replace(" ", "-")
		new_array = new_array.split(",")
		player_array = []
		player_array = new_array
	return player_array


def main():

	print("Starting to scrape...")
	print('...')


	cur, conn = dbase_init()

	player_array = some_or_all()


	print("Chicago Bulls Roster: ")

	scrape(player_array, cur)
	
	print()

	stop = query_interface(cur, conn)
	if stop == True:
		return

	# close database connection
	cur.close()
	conn.commit()
	conn.close()

main()