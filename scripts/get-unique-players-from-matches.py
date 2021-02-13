import pandas as pd
import numpy as np


def createCsvOfUniquePlayerIds(inputCsv, outCsv):
    dataset = pd.read_csv(inputCsv)
    uniqueWinners = dataset.winner_id.unique()
    uniqueLosers = dataset.loser_id.unique()
    winnersAndLosers = np.concatenate((uniqueWinners, uniqueLosers))
    uniqueIds = np.unique(winnersAndLosers)

    return uniqueIds

    df = pd.DataFrame({'player_id': uniqueIds[:]})
    df.to_csv(outCsv)

playersFor2018 = createCsvOfUniquePlayerIds('./data/atp_matches_2018.csv', './data/C_players_2018.csv')

playersFor2019 = createCsvOfUniquePlayerIds('./data/atp_matches_2019.csv', './data/C_players_2019.csv')

playersFor2020 = createCsvOfUniquePlayerIds('./data/atp_matches_2020.csv', './data/C_players_2020.csv')

allPlayers = np.concatenate((playersFor2018, playersFor2019, playersFor2020))
uniqueAllPlayers = np.unique(allPlayers)


df = pd.DataFrame({'player_id': uniqueAllPlayers[:]})
# df.to_csv('./data/HC_unique_players.csv')

# print('There are ', df.size, ' unique players')



allPlayersDf = pd.read_csv('./data/atp_players.csv', header=None)
allPlayersDf = allPlayersDf[allPlayersDf[0].isin()] 
allPlayersDf = allPlayersDf.drop(allPlayersDf[~allPlayersDf[0].isin(values=uniqueAllPlayers.tolist())].index)

# allPlayersDf = allPlayersDf.apply(lambda x: np.nan if !isinstance(x[0], uniqueAllPlayers) else x).dropna(subset=[0]);

print(allPlayersDf.head())
