import pandas as pd

def _sum(arr):  
    sum=0
    for i in arr: 
        sum = sum + i 
    return(sum)
#78 100644 2020
dataset2018 = pd.read_csv('./data/HC_players_2018.csv')
dataset2019 = pd.read_csv('./data/HC_players_2019.csv')
dataset2020 = pd.read_csv('./data/HC_players_2020.csv')
datasetAll = pd.read_csv('./data/HC_players_all.csv')
df2018 = pd.DataFrame(dataset2018)
df2019 = pd.DataFrame(dataset2019)
df2020 = pd.DataFrame(dataset2020)
dfAll = pd.DataFrame(datasetAll)
playerCount2018 = []
playerCount2019 = []
playerCount2020 = []
playerCount = []
datasetMatches2018 = pd.read_csv('./data/atp_matches_2018.csv')
dfMatches2018 = pd.DataFrame(datasetMatches2018)
datasetMatches2019 = pd.read_csv('./data/atp_matches_2019.csv')
dfMatches2019 = pd.DataFrame(datasetMatches2019)
datasetMatches2020 = pd.read_csv('./data/atp_matches_2020.csv')
dfMatches2020 = pd.DataFrame(datasetMatches2020)
#progress = 0
for d in df2018.itertuples():
    #progress += 1
    #print(progress)
    playerOpponents2018 = []
    for d2 in dfMatches2018.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponents2018)):
            playerOpponents2018.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponents2018))) :
            playerOpponents2018.append(d2[8])
    playerCount2018.append(len(playerOpponents2018))
df2018['6'] = playerCount2018
df2018 = df2018.sort_values(by=['6'], ascending=False)
#progress = 0
for d in df2019.itertuples():
    #progress += 1
    #print(progress)
    playerOpponents2019 = []
    for d2 in dfMatches2019.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponents2019)):
            playerOpponents2019.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponents2019))) :
            playerOpponents2019.append(d2[8])
    playerCount2019.append(len(playerOpponents2019))
df2019['6'] = playerCount2019
df2019 = df2019.sort_values(by=['6'], ascending=False)
#progress = 0
for d in df2020.itertuples():
    #progress += 1
    #print(progress)
    playerOpponents2020 = []
    for d2 in dfMatches2020.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponents2020)):
            playerOpponents2020.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponents2020))) :
            playerOpponents2020.append(d2[8])
    playerCount2020.append(len(playerOpponents2020))
df2020['6'] = playerCount2020
df2020 = df2020.sort_values(by=['6'], ascending=False)
#progress = 0
for d in dfAll.itertuples():
    #progress += 1
    #print(progress)
    playerOpponentsAll = []
    for d2 in dfMatches2018.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponentsAll)):
            playerOpponentsAll.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponentsAll))) :
            playerOpponentsAll.append(d2[8])
    for d2 in dfMatches2019.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponentsAll)):
            playerOpponentsAll.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponentsAll))) :
            playerOpponentsAll.append(d2[8])
    for d2 in dfMatches2019.itertuples():
        if((d[1] == d2[8]) and not (d2[16] in playerOpponentsAll)):
            playerOpponentsAll.append(d2[16])
        elif (((d[1] == d2[16]) and not (d2[8] in playerOpponentsAll))) :
            playerOpponentsAll.append(d2[8])
    playerCount.append(len(playerOpponentsAll))
dfAll['6'] = playerCount
dfAll = dfAll.sort_values(by=['6'], ascending=False)
print('REZULTATI 2018:\n', df2018[['1', '2', '6']].head(6) )
print('REZULTATI 2019:\n',df2019[['1', '2', '6']].head(6) )
print('REZULTATI 2020:\n',df2020[['1', '2', '6']].head(6) )
print('REZULTATI TOTAL:\n',dfAll[['1', '2', '6']].head(6) )
