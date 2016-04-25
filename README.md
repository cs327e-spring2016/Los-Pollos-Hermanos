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

Tables: 

- create table Data (id_pk INT not null, game_fk INT, player_fk INT, minutes INT, fg_made INT, fg_attempted INT, three_made INT, three_attempted INT, free_made INT, free_attempted INT, rebounds INT, assists INT, blocks INT, steals INT, fouls INT, turnovers INT, points INT, PRIMARY KEY (id_pk));

- create table Games ( id_pk INT not null, opponent_fk INT, location varchar(25), date varchar(25), score varchar(25), PRIMARY KEY (id_pk));

- create table Player (id_pk INT not null, first varchar(25), last varchar(25), age INT, PRIMARY KEY (id_pk));

- create table Opponents (id_pk INT not null, name varchar(25), PRIMARY KEY (id_pk));


Update April 24, 2016

- All data is successfully being scraped
- Scraped data is correctly introduces into database
- First custom query integration is complete -- Currently only queries one table at a time

Update April 25, 2016

- game id bug fixed. Ready for M5
