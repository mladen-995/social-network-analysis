import pandas as pd
import numpy as np


def createCsvOfUniquePlayerIdsFromPlayers(inputCsv):
    dataset = pd.read_csv(inputCsv)
    uniqueWinners = dataset.winner_id.unique()
    uniqueLosers = dataset.loser_id.unique()
    winnersAndLosers = np.concatenate((uniqueWinners, uniqueLosers))
    uniqueIds = np.unique(winnersAndLosers)
    return uniqueIds
    
def createCsvOfUniquePlayerIdsFromRankings(inputCsv, hasHeader):
    if(hasHeader):
        dataset = pd.read_csv(inputCsv)
        uniquePlayers = dataset.player.unique()
    else:
        dataset = pd.read_csv(inputCsv, header=None)
        uniquePlayers = dataset[2].unique()
    return uniquePlayers


def filterPlayersByPlayerList(outputCsv, playerList):
    playersDf = pd.read_csv('./data/atp_players.csv', header=None)
    playersDfFinal = playersDf.drop(playersDf[~playersDf[0].isin(playerList)].index)
    playersDfFinal.to_csv(outputCsv, index=False)


playersFor2018 = createCsvOfUniquePlayerIdsFromPlayers('./data/atp_matches_2018.csv')

playersFor2019 = createCsvOfUniquePlayerIdsFromPlayers('./data/atp_matches_2019.csv')

playersFor2020 = createCsvOfUniquePlayerIdsFromPlayers('./data/atp_matches_2020.csv')

allPlayers = np.concatenate((playersFor2018, playersFor2019, playersFor2020))
uniqueAllPlayers = np.unique(allPlayers)

filterPlayersByPlayerList('./data/HC_players_2018.csv', playersFor2018)
filterPlayersByPlayerList('./data/HC_players_2019.csv', playersFor2019)
filterPlayersByPlayerList('./data/HC_players_2020.csv', playersFor2020)
filterPlayersByPlayerList('./data/HC_players_all.csv', uniqueAllPlayers)


players10s = createCsvOfUniquePlayerIdsFromRankings('./data/atp_rankings_10s.csv', True)

playersCurrent = createCsvOfUniquePlayerIdsFromRankings('./data/atp_rankings_current.csv', False)

allPlayersFromRankings = np.concatenate((players10s, playersCurrent))
uniqueAllPlayersFromRankings = np.unique(allPlayersFromRankings)

filterPlayersByPlayerList('./data/HC_players_from_rankings_10s.csv', players10s)
filterPlayersByPlayerList('./data/HC_players_from_rankings_current.csv', playersCurrent)
filterPlayersByPlayerList('./data/HC_players_from_rankings_all.csv', uniqueAllPlayersFromRankings)

uniquePlayers201810s = np.unique(np.intersect1d(players10s, playersFor2018))
uniquePlayers201910s = np.unique(np.intersect1d(players10s, playersFor2019))
uniquePlayers202010s = np.unique(np.intersect1d(players10s, playersFor2020))
uniquePlayersAll10s = np.unique(np.intersect1d(players10s, uniqueAllPlayers))

filterPlayersByPlayerList('./data/HC_players_from_matches2018_and_rankings10s.csv', uniquePlayers201810s)
filterPlayersByPlayerList('./data/HC_players_from_matches2019_and_rankings10s.csv', uniquePlayers201910s)
filterPlayersByPlayerList('./data/HC_players_from_matches2020_and_rankings10s.csv', uniquePlayers202010s)
filterPlayersByPlayerList('./data/HC_players_from_matchesAll_and_rankings10s.csv', uniquePlayersAll10s)

uniquePlayers2018Current = np.unique(np.intersect1d(playersCurrent, playersFor2018))
uniquePlayers2019Current = np.unique(np.intersect1d(playersCurrent, playersFor2019))
uniquePlayers2020Current = np.unique(np.intersect1d(playersCurrent, playersFor2020))
uniquePlayersAllCurrent = np.unique(np.intersect1d(playersCurrent, uniqueAllPlayers))

filterPlayersByPlayerList('./data/HC_players_from_matches2018_and_rankingsCurrent.csv', uniquePlayers201810s)
filterPlayersByPlayerList('./data/HC_players_from_matches2019_and_rankingsCurrent.csv', uniquePlayers2019Current)
filterPlayersByPlayerList('./data/HC_players_from_matches2020_and_rankingsCurrent.csv', uniquePlayers2020Current)
filterPlayersByPlayerList('./data/HC_players_from_matchesAll_and_rankingsCurrent.csv', uniquePlayersAllCurrent)

uniquePlayers2018All = np.unique(np.intersect1d(uniqueAllPlayersFromRankings, playersFor2018))
uniquePlayers2019All = np.unique(np.intersect1d(uniqueAllPlayersFromRankings, playersFor2019))
uniquePlayers2020All = np.unique(np.intersect1d(uniqueAllPlayersFromRankings, playersFor2020))
uniquePlayersAllAll = np.unique(np.intersect1d(uniqueAllPlayersFromRankings, uniqueAllPlayers))

filterPlayersByPlayerList('./data/HC_players_from_matches2018_and_rankingsAll.csv', uniquePlayers2018All)
filterPlayersByPlayerList('./data/HC_players_from_matches2019_and_rankingsAll.csv', uniquePlayers2019All)
filterPlayersByPlayerList('./data/HC_players_from_matches2020_and_rankingsAll.csv', uniquePlayers2020All)
filterPlayersByPlayerList('./data/HC_players_from_matchesAll_and_rankingsAll.csv', uniquePlayersAllAll)

#print('Number of filtered players ', len(allPlayersDfFinal.index))
