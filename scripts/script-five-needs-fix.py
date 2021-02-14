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

datasetAll = pd.read_csv('./data/HC_players_from_matchesAll_and_rankingsAll.csv')
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

datasetRankings10s = pd.read_csv('./data/atp_rankings_10s.csv')
dfRankings10s = pd.DataFrame(datasetRankings10s)

datasetRankingsCurrent = pd.read_csv('./data/atp_rankings_current.csv')
dfRankingsCurrent = pd.DataFrame(datasetRankingsCurrent)
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
    for d1 in dfRankings10s.itertuples():
        ranks2010 = []
        ranks2011 = []
        ranks2012 = []
        ranks2013 = []
        ranks2014 = []
        ranks2015 = []
        ranks2016 = []
        ranks2017 = []
        ranks2018 = []
        ranks2019 = []
        if(d1[3] == d[1]):
            print(_formatDate(d1[1]), d1[2])
            year = d1[1] // 10000
            if(year == 2010):
                ranks2010.append(d1[2])
            elif(year == 2011):
                ranks2011.append(d1[2])
            elif(year == 2012):
                ranks2012.append(d1[2])
            elif(year == 2013):
                ranks2013.append(d1[2])
            elif(year == 2014):
                ranks2014.append(d1[2])
            elif(year == 2015):
                ranks2015.append(d1[2])
            elif(year == 2016):
                ranks2016.append(d1[2])
            elif(year == 2017):
                ranks2017.append(d1[2])
            elif(year == 2018):
                ranks2018.append(d1[2])
            elif(year == 2019):
                ranks2019.append(d1[2])
    ranks2020 = []
    for d1 in dfRankingsCurrent.itertuples():
        if(d1[3] == d[1]):
            print(_formatDate(d1[1]), d1[2])
            ranks2020.append(d1[2])
    averageRatingTotal = []
    if len(ranks2010) > 0 : averageRatingTotal.append(_sum(ranks2010) / len(ranks2010))
    if len(ranks2011) > 0 : averageRatingTotal.append(_sum(ranks2011) / len(ranks2011))
    if len(ranks2012) > 0 : averageRatingTotal.append(_sum(ranks2012) / len(ranks2012))
    if len(ranks2013) > 0 : averageRatingTotal.append(_sum(ranks2013) / len(ranks2013))
    if len(ranks2014) > 0 : averageRatingTotal.append(_sum(ranks2014) / len(ranks2014))
    if len(ranks2015) > 0 : averageRatingTotal.append(_sum(ranks2015) / len(ranks2015))
    if len(ranks2016) > 0 : averageRatingTotal.append(_sum(ranks2016) / len(ranks2016))
    if len(ranks2017) > 0 : averageRatingTotal.append(_sum(ranks2017) / len(ranks2017))
    if len(ranks2018) > 0 : averageRatingTotal.append(_sum(ranks2018) / len(ranks2018))
    if len(ranks2019) > 0 : averageRatingTotal.append(_sum(ranks2019) / len(ranks2019))
    if len(ranks2020) > 0 : averageRatingTotal.append(_sum(ranks2020) / len(ranks2020))
    print('Prosečni rang:', _sum(averageRatingTotal) / len(averageRatingTotal))
    
