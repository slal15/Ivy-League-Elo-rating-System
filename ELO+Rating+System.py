
# coding: utf-8

# In[2]:

import math

def calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament):
    
    k = 7.054 #From backtesting k-values
    if Ivy_Season == 'Y' :
        k = 12.944  #From backtesting k-values
    
    #Accounts for those teams being very good
    if NCAA_Tournament == 'Y':
        k = 17.944 #+5 is arbitrary
        away_team_elo == 1700 #Rating is arbitrary estimation
    
    #Adjusting variable for home court advantage
    Real_Home_Game = 0
    if Location != '': #Otherwise description of actual location
        if Ivy_Season == 'Y':
            Real_Home_Game = 62.71 #Based on in Ivy home win % of 58.93
        else:
            Real_Home_Game = 120.04 #Based on out of Ivy win % of 66.62 
    
    
    #Actual Calculations
    home_ELODIFF = (home_team_elo+Real_Home_Game - away_team_elo)
    away_ELODIFF = (away_team_elo-home_team_elo-Real_Home_Game)
    
    home_expected_outcome = float(1/(10**(-home_ELODIFF/400)+1))
    away_expected_outcome = float(1/(10**(-away_ELODIFF/400)+1))
        
    actual_home_outcome = 0
    actual_away_outcome = 0
        
    actual_home_outcome = 0
    actual_away_outcome = 0
    
    if MOV >0:        
        actual_home_outcome = 1
        ELOW = home_team_elo
        ELOL = away_team_elo
    else:
        actual_away_outcome = 1
        ELOW = away_team_elo
        ELOL = home_team_elo
    
    
    MOV_Multiplier = math.log((math.fabs(MOV)+1) * (2.2/((ELOW-ELOL)*.001+2.2))) #Based on 538's analysis
    
    new_home_ELO = home_team_elo + MOV_Multiplier * k * (actual_home_outcome - (home_expected_outcome))
    new_away_ELO = away_team_elo + MOV_Multiplier * k * (actual_away_outcome - (away_expected_outcome))
    
    new_values = [new_home_ELO, new_away_ELO]
        
    return new_values


def Find_Current_ELO(f):
    in_file = open(f)
    
    content = in_file.read()
    
    lines = content.split('\n') #List where each element is a string that represents a game
    events = [[]]
    del events[0] #CSV first line is just headers
    
    elo_ratings = {}
    
    team_names = set()
    
    #Each line is a single game
    for n in range (1,len(lines)):
        single_game = lines[n].split(',')
        events.append(single_game)    
    
    #Getting all team names
    for i in range (0,len(events)):
        team_names.add(str(events[i][4]))
        team_names.add(str(events[i][6]))
    
    #Initializing ratings for each team
    for element in team_names:
        elo_ratings[element] = 1500
    
    
    
    #Calculating new ELO as a result of each game
    
    #Update for 2012 season — Double check ranges
    for j in range (0,188):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        
        #if j== 187 :
        #    print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])
        
    #Revert to mean
    for key in elo_ratings:
        elo_ratings[key] = elo_ratings[key]*.75+1500*.25
    
    
    #Update for 2013 season — Double check ranges 
    for j in range (188,367):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        
        #if j== 366 :
        #    print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])
        
        
    #Revert to mean
    for key in elo_ratings:
        elo_ratings[key] = elo_ratings[key]*.75+1500*.25
    
    
    #Update for 2014 season — Double check ranges 
    for j in range (367,552):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        
        #if j== 551 :
        #    print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])
        
    #Revert to mean
    for key in elo_ratings:
        elo_ratings[key] = elo_ratings[key]*.75+1500*.25    

    
    #Update for 2015 season — Double check ranges 
    for j in range (552,733):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        
        #if j== 732 :
        #    print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])
        
    #Revert to mean
    for key in elo_ratings:
        elo_ratings[key] = elo_ratings[key]*.75+1500*.25   
        
    
    #Update for 2016 season — Double check ranges 
    for j in range (733,913):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        
        #if j== 912 :
        #    print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])
        
    #Revert to mean
    for key in elo_ratings:
        elo_ratings[key] = elo_ratings[key]*.75+1500*.25
        
        
    #Update for 2017 season *Note no mean reversion
    for j in range (913,1076):    
        curr_event = []
        
        for k in range (0,len(events[0])):
            curr_event.append(events[j][k]) 
        if j== 1075 :
            print('Current event:', curr_event)
            
        home_team_name = str(curr_event[6])
        away_team_name = str(curr_event[4])
        home_team_elo = elo_ratings[home_team_name]
        away_team_elo = elo_ratings[away_team_name]
        MOV = int(curr_event[12])
        Location = str(curr_event[13])
        Ivy_Season = str(curr_event[2])
        NCAA_Tournament = str(curr_event[3])
        
        #Updating teams' elo ratings
        new_values = calc_elo(home_team_elo,away_team_elo,MOV,Location,Ivy_Season,NCAA_Tournament)
        elo_ratings[home_team_name] = int(new_values[0])
        elo_ratings[away_team_name] = int(new_values[1])    
    
        
    
    for key in elo_ratings:
        if key == 'Columbia' or key == 'Yale' or key == 'Dartmouth' or key =='Princeton':
            s = key + ' ' + str(elo_ratings[key])
            print(s)
        elif key == 'Penn' or key == 'Harvard' or key == 'Cornell' or key == 'Brown':
            s = key + ' ' + str(elo_ratings[key])
            print(s)

        else:
            continue
    
    for home_team_name in elo_ratings:
        global expected_wins
        expected_wins = 0
        if home_team_name == 'Columbia' or home_team_name == 'Yale' or home_team_name == 'Dartmouth' or home_team_name =='Princeton' or home_team_name == 'Penn' or home_team_name == 'Harvard' or home_team_name == 'Cornell' or home_team_name == 'Brown' :
            for other_key in elo_ratings:
                if other_key == 'Columbia' or other_key == 'Yale' or other_key == 'Dartmouth' or other_key =='Princeton' or other_key == 'Penn' or other_key == 'Harvard' or other_key == 'Cornell' or other_key == 'Brown' :
                    if home_team_name != other_key:
                        home_ELODIFF = elo_ratings[home_team_name]+ 47.69 - elo_ratings[other_key]
                        expected_win_probability = float(1/(10**(-home_ELODIFF/400)+1))
                        expected_wins = expected_wins+ expected_win_probability
            
            #Play both home and away series against every team
            for another_key in elo_ratings:
                if another_key == 'Columbia' or another_key == 'Yale' or another_key == 'Dartmouth' or another_key =='Princeton' or another_key == 'Penn' or another_key == 'Harvard' or another_key == 'Cornell' or another_key == 'Brown' :
                    if home_team_name != other_key:
                        away_ELODIFF = elo_ratings[home_team_name]- 47.69 - elo_ratings[other_key]
                        expected_win_probability = float(1/(10**(-away_ELODIFF/400)+1))
                        expected_wins = expected_wins+ expected_win_probability
            print(home_team_name, ' ', expected_wins)
    
    return None

if __name__ == '__main__':
    Find_Current_ELO('Raw ELO Data 3-06-17 EOS.csv')


# In[ ]:



