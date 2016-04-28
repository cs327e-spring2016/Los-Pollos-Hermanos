from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/games")
def getGames():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')
	cur = conn.cursor()
	arrayTo = []
	hfg = cur.execute('SELECT %s FROM %s' % ("*", "Games"))
	p = cur.fetchall()
	for row in p:
		ntstr = [row[0],row[1], row[2], row[3], row[4]]
		arrayTo.append(ntstr)
	return render_template("games.html", player_array= arrayTo)


@app.route("/players")
def getPlayers():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')
	cur = conn.cursor()
	arrayTo = []
	hfg = cur.execute('SELECT %s FROM %s' % ("*", "Player"))
	p = cur.fetchall()
	for row in p:
		ntstr = [row[0],row[1], row[2], row[3]]
		arrayTo.append(ntstr)
	return render_template("players.html", player_array= arrayTo)

@app.route("/data")
def getData():
	conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jfh71293.,', db='data_scraper')
	cur = conn.cursor()
	arrayT = []
	hfg = cur.execute('SELECT %s FROM %s' % ("*", "Data"))
	p = cur.fetchall()
	for row in p:
		ntstr = [row[0],row[1], row[2], row[3], row[4],row[5], row[6], row[7], row[8],row[9], row[10], row[11], row[12],row[13], row[14], row[15], row[16],row[17]]
		arrayT.append(ntstr)
	return render_template("data.html", player_array= arrayT)




if __name__ == "__main__":
    app.run(debug=True)
