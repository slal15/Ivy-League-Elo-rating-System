# Ivy-League-Elo-rating-System

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


### Number of events:
A CSV file composed of the results of the previous 5 seasons of Ivy teams' results was compiled (see weakness of this below). After each season, each team's Elo rating reverts back to the mean of 1500, as a quarter of the team in theory graduates. 


### Further work to improve system:
* Second game of back to back road games. 
  *Explore whether teams playing a second consecutive road game disproportiantely lose, could improve prediction system.

* Include all games of non-conference teams to have more accurate results. 
 *Currently only Ivy team's results are included but inherently the out of conference results will not be accurate in updating Elo ratings, as team's like Duke are considered an average of 1500 rather than a rating more commensurate with actual ability.

* Build Monte Carlo simulation that updates with each result throughout season
