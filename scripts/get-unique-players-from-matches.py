import pandas as pd
import numpy as np


def createCsvOfUniquePlayerIds(inputCsv, outCsv):
    dataset = pd.read_csv(inputCsv)
    uniqueWinners = dataset.winner_id.unique()
    uniqueLosers = dataset.loser_id.unique()
    winnersAndLosers = np.concatenate((uniqueWinners, uniqueLosers))
    uniqueIds = np.unique(winnersAndLosers)

    df = pd.DataFrame({'player_id': uniqueIds[:]})
    df.to_csv(outCsv)

    return uniqueIds

playersFor2018 = createCsvOfUniquePlayerIds('./data/atp_matches_2018.csv', './data/HC_players_2018.csv')

playersFor2019 = createCsvOfUniquePlayerIds('./data/atp_matches_2019.csv', './data/HC_players_2019.csv')

playersFor2020 = createCsvOfUniquePlayerIds('./data/atp_matches_2020.csv', './data/HC_players_2020.csv')

allPlayers = np.concatenate((playersFor2018, playersFor2019, playersFor2020))
uniqueAllPlayers = np.unique(allPlayers)


df = pd.DataFrame({'player_id': uniqueAllPlayers[:]})

allPlayersDf = pd.read_csv('./data/atp_players.csv', header=None)
allPlayersDfFinal = allPlayersDf.drop(allPlayersDf[~allPlayersDf[0].isin(uniqueAllPlayers)].index)

allPlayersDfFinal.to_csv('./data/HC_players_all.csv')


print('Number of filtered players ', len(allPlayersDfFinal.index))
