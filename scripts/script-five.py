import pandas as pd
def _formatDate(date):
    year = date//10000
    month = (date%10000)//100
    day = date%100
    return str(day) + '/' + str(month) + '/' + str(year)
def _sum(arr):  
    sum=0
    for i in arr: 
        sum = sum + i 
    return(sum)
datasetAll = pd.read_csv('./data/HC_players_from_matchesAll_and_rankingsCurrent.csv')
dfAll = pd.DataFrame(datasetAll)
playerCount = []
datasetMatches2018 = pd.read_csv('./data/atp_matches_2018.csv')
dfMatches2018 = pd.DataFrame(datasetMatches2018)
datasetMatches2019 = pd.read_csv('./data/atp_matches_2019.csv')
dfMatches2019 = pd.DataFrame(datasetMatches2019)
datasetMatches2020 = pd.read_csv('./data/atp_matches_2020.csv')
dfMatches2020 = pd.DataFrame(datasetMatches2020)
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

datasetRankings = pd.read_csv('./data/atp_rankings_current.csv')
dfRankings = pd.DataFrame(datasetRankings)
dfAll = dfAll[:10]
first = True
for d in dfAll.itertuples():  
    if(~first):
        print('-----------------------')
    else:
        first = False
    print('Teniser:', d[2], d[3])
    print('Datum i rang:')
    rankings = []
    for d1 in dfRankings.itertuples():
        if(d1[3] == d[1]):
            print(_formatDate(d1[1]), d1[2])
            rankings.append(d1[2])
    print('Prosečni rang:', _sum(rankings) / len(rankings))
    
