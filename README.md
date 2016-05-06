#LosPollosHermanos
Team Members: Juan Hinojosa, Leonel Rodriguez, Wei Da Pan

- Grab data from sports sites, basketball
- Analyze team performance data
- Analyze player performance data per game
- Compare both data to view player value to team(overall points, rebounds, 3 pointers, fouls, time played)

#
Database details:

Database name: 
data_scraper

Tables: Updated(04/26)

- create table Data (id_pk INT not null, game_fk INT, player_fk INT, minutes INT, fg_made INT, fg_attempted INT, three_made INT, three_attempted INT, free_made INT, free_attempted INT, rebounds INT, assists INT, blocks INT, steals INT, fouls INT, turnovers INT, points INT, outcome varchar(1), PRIMARY KEY (id_pk));

- create table Games ( id_pk INT not null, opponent_fk varchar(25), date varchar(25), score varchar(25), outcome varchar(1), PRIMARY KEY (id_pk));

- create table Player (id_pk INT not null, first varchar(25), last varchar(25), age INT, PRIMARY KEY (id_pk));



Update April 24, 2016

- All data is successfully being scraped
- Scraped data is correctly introduces into database
- First custom query integration is complete -- Currently only queries one table at a time

Update April 25, 2016

- game id bug fixed. Ready for M5

Update April 26, 2016

- refreshed code. bug fixes in teams imports and games

Update May 5, 2016

- data scraping: 100%
- database: 100%
- front end: 100%

Requirements to test app locally

- start up MySQL and create database name "data_scraper"
- edit functions in app.py and input your MySQL root password
- install additional python package virtualenv and flask
- activate virtualenv FlaskApp
- run python3 app.py
- open browser and go to 0.0.0.0:8081
- click to import data, wait, and enjoy
- fun query to test is "SELECT CONCAT(P.first,' ',P.last), G.opponent_fk, G.date, P.age, D.minutes, D.fg_made, D.fg_attempted, D.three_made, D.three_attempted, D.free_made, D.free_attempted, D.points, D.outcome FROM Data D INNER JOIN Player P ON D.player_fk = P.id_pk INNER JOIN Games G ON D.game_fk = G.id_pk"
- to test app wit console interface do the following
- edit heisenberg.py and add your MySQL root password
- run python3 heisenberg.py and enjoy

- our application is also remotely accesible from the public IP http://54.183.231.13/

