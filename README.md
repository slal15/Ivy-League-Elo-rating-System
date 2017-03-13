# Ivy-League-Elo-rating-System

### Background on Elo (from Wikipedia)
It is a method for calculating the relative skill levels of players in competitor-versus-competitor games such as chess. It is named after its creator Arpad Elo, a Hungarian-born American physics professor.

The difference in the ratings between two players serves as a predictor of the outcome of a match. Two players with equal ratings who play against each other are expected to score an equal number of wins. A player whose rating is 100 points greater than their opponent's is expected to score 64%; if the difference is 200 points, then the expected score for the stronger player is 76%.

A player's Elo rating is represented by a number which increases or decreases depending on the outcome of games between rated players. After every game, the winning player takes points from the losing one. The difference between the ratings of the winner and loser determines the total number of points gained or lost after a game. In a series of games between a high-rated player and a low-rated player, the high-rated player is expected to score more wins. If the high-rated player wins, then only a few rating points will be taken from the low-rated player. However, if the lower rated player scores an upset win, many rating points will be transferred. The lower rated player will also gain a few points from the higher rated player in the event of a draw. This means that this rating system is self-correcting. A player whose rating is too low should, in the long run, do better than the rating system predicts, and thus gain rating points until the rating reflects their true playing strength.


## Our system
This system is based off of the chess rating system and inspired from 538. It attempts to calculate the Elo ratings of only the teams playing in the Ivy League, as the only predictions made from the system are the Ivy League season (see bottom for coverage). 

There are two components to the program: the individual updating of Elo ratings from a single game's results and the number of events included.

### Individual updating of Elo ratings (calc_elo function):
The updating of values comes from chess itself where there is a comparison between the expected outcome, determined via Elo ratings before contest, and the actual outcome. The expected outcome is directly from the original chess system except for one factor, a home-court advantage. 

##### Home Court Advantage
* The logic behind giving teams at a home boost is derived from Ivy conference games see the home team win 58.93%, while non-conference games see the home team win 66.62% of games in our 1000+ game sample size. It is assumed that there is an even distribution of good teams playing home and away, as opposed to better teams disproportiantely playing at home. From these win percentages we can deduce the boost that a team should get such that if two evenly rated teams play, the home team should win according to those percentages.

After the difference between expected and actual outcome is calculated it is then multiplied by several factors to determine how much the two team's Elo ratings will go up or down after the event (Note. a team's loss in Elo points will be equal to the other team's gain in points). The factors are: Margin of Victory and K-factor.

##### MOV and K-Factor
* Margin of victory is from 538's NFL Elo system. The larger the MOV the larger the impact of the game. There are diminishing returns as ln(MOV) is taken.

* K-Factor was determined via backtesting on the previous five seasons of Ivy play. Since the system was intended to predict the outcomes of the Ivy regular season, the idea is that Ivy games would be better at predicting future success then out of conference games, which is why there is an Ivy and non-Ivy k-value. The specific values were determined by iterating through values 1-20 for each and taking a weighted average of those that would result in the optimal number of picks in a particular season. For example the system would have picked 46 out of 56 Ivy games prior to the start of the 2013 Ivy season if the Ivy k-value is 19.5 and the out of Ivy K was 3. This means Ivy games from previous seasons were waited more than 6 times as much as out of conference games.


### Number of events (find_current_elo(f)):
This function takes in a CSV file composed of the results of the previous 5 seasons of Ivy teams' results was compiled (see weakness of this below). Each team that shows up in these events is added to dictionary and initialized to an Elo rating of 1500. Each event is then iterated through and the Elo values of the two teams involved are updated after the results. After each season ~300 games, each team's Elo rating reverts back to the mean of 1500 25%, as a quarter of the team in theory graduates. 


### 2016-2017 Ivy League Results
System "picked" 35 out of 50 games correctly. A correct pick is a team that was forcasted >50% chance of winning game and won. The expected value of the 50 picks made was 34.5.  


### Rating System in action for *Columbia Daily Spectator*
* http://columbiaspectator.com/sports/2017/01/19/spectators-new-statistical-approach-projecting-mens-ivy-basketball-season/
* http://columbiaspectator.com/sports/2017/02/23/elo-forecasts-crucial-week-eight-of-ivy-mens-basketball/
* http://columbiaspectator.com/sports/2017/03/10/elos-goodbye-to-mens-basketballs-2017-ivy-season/

### Further work to improve system:
* Second game of back to back road games. Explore whether teams playing a second consecutive road game disproportiantely lose, could improve prediction system.

* Include all games of non-conference teams to have more accurate results. Currently only Ivy team's results are included but inherently the out of conference results will not be accurate in updating Elo ratings, as team's like Duke are considered an average of 1500 rather than a rating more commensurate with actual ability.

* Build Monte Carlo simulation that updates with each result throughout season
