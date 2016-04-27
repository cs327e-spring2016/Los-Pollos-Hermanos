from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


preseason =["Fri 10/23","Tue 10/20","Mon 10/19","Wed 10/14","Mon 10/12","Sat 10/10","Thu 10/8","Tue 10/6"]
Division=[5,8,11,15,1,14,18,20,28,30] #x4
OtherCon = [3, 6, 7, 9, 10,12,13,16,21,22,23,24,25,26,29] #x2
Conf=[2,17,19,27]	#x3

def dbase_init():
	# database connection: add your own passwd
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')
	cur = conn.cursor()



	# tables wiped 

	cur.execute("DELETE FROM Data")
	cur.execute("DELETE FROM Player")
	cur.execute("DELETE FROM Games")



	return cur, conn


def scrape(player_array, cur):
	global globalid_num
	global game_id
	global oppo_bool
	global data_id

	id_num = 0
	globalid_num = 0
	game_id = 0
	oppo_bool = False
	data_id = 0
	# iterate over roster
	for plyer in range(1,(len(player_array)+1)):

		game_id = 0


		ayer = player_array[plyer-1]
		ayer = ayer.split("-")

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
		for v in range(1,31):
			odd(v, bsObj, playr, player, ayer, cur, plyer)
			even(v, bsObj, playr, player, ayer,cur, plyer)

		print("Player: ", ayer[0].capitalize(), ayer[1].capitalize(),"is done!")


def odd(v, bsObj, playr, player, ayer,cur, plyer):
	global data_id
	global game_id
	global dates
	dates = [0]*82
	xy=0
	v = str(v)
	st1 = (bsObj.findAll("tr", {"class":"oddrow team-46-"+v}))


	for i in range(len(st1)):


		obj = st1[i].findAll("td")
		playr = player.split("-")
		
		#date
		date = obj[0].getText()
		if date in preseason:
			continue
		if date in dates:
			continue

		game_id += 1
		data_id += 1

		dates[xy]=date
		xy+=1

		#opponent
		opp = obj[1].getText()
		opponent = opp[2:]
		#score
		q = obj[2].findAll("a")
		score = q[0].getText()
		#outcome
		wl = obj[2].findAll("span")
		outcome = wl[0].getText()
		#minutes
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
			cur.execute('insert into Games values (%s,"%s","%s","%s","%s")' % (game_id, opponent , date, score, outcome))
		cur.execute('insert into Data values ("%s",%s,%s,"%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s", "%s")' % (data_id, game_id ,plyer, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points, outcome ))
	# end of scrape


def even(v, bsObj, playr, player, ayer,cur, plyer):
	global data_id
	global game_id

	xy = 0
	v = str(v)
	st2 = (bsObj.findAll("tr", {"class":"evenrow team-46-"+v}))


	for i in range(len(st2)):
		obj = st2[i].findAll("td")
		playr = player.split("-")
		#date
		date = obj[0].getText()
		if date in preseason:
			continue
		if date in dates:
			continue

		game_id += 1
		data_id += 1
		dates[xy]=date
		xy+=1
		#opponent
		opp = obj[1].getText()
		opponent = opp[2:]
		#score
		q = obj[2].findAll("a")
		score = q[0].getText()
		#outcome
		wl = obj[2].findAll("span")
		outcome = wl[0].getText()
		#minutes
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
			cur.execute('insert into Games values (%s,"%s","%s","%s","%s")' % (game_id, opponent , date, score, outcome))
		cur.execute('insert into Data values ("%s",%s,%s,"%s", "%s", "%s","%s","%s","%s", "%s" ,"%s", "%s", "%s","%s","%s","%s", "%s", "%s")' % (data_id, game_id ,plyer, minu, fg_made, fg_attempted, three_made, three_attempted, free_made, free_attempted, rebounds, assists, blocks, steals, fouls, turnovers, points, outcome ))
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
			print("Table", table.capitalize(), "has: outcome, id_pk , game_fk , player_fk , minutes  , fg_made , fg_attempted , three_made , three_attempted , free_made , free_attempted , rebounds , assists , blocks , steals , fouls , turnovers ,  points for each Player in each Game played")
			print()
			select = input("What would you like to select(use commas to separate values)? ")
			select2 = select.split(",")
			print(select)
			c = False
		elif (table.lower() == "games"):
			print("Table", table.capitalize(), "has: outcome, id_pk , opponent_fk , date , and score for each game")
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
