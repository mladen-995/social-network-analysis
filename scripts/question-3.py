import pandas as pd
import numpy as np


def get_number_of_tourneys_per_player(matchesDf, n):
    groupedByTourney = matchesDf.groupby('tourney_id')
    playersPerTourney = pd.DataFrame(columns=['tourney_id', 'player_id'])

    for tourney_id, players in groupedByTourney:
        winner_ids = players.winner_id.unique()
        loser_ids = players.loser_id.unique()

        playerIds = np.concatenate((winner_ids, loser_ids), axis=0)
        playerIds = np.unique(playerIds)

        playerIdsDf = pd.DataFrame({
            'tourney_id': np.repeat(tourney_id, playerIds.size),
            'player_id': playerIds
        })

        playersPerTourney = playersPerTourney.append(playerIdsDf)

    groupedByPlayer = playersPerTourney.groupby('player_id')

    numberOfTourneysPerPlayer = pd.DataFrame(columns=['player_id', 'number_of_tourneys'])


    for player_id, tourneys in groupedByPlayer:
        df = pd.DataFrame({
            'player_id': [player_id],
            'number_of_tourneys': [tourneys.shape[0]]
        })

        numberOfTourneysPerPlayer = numberOfTourneysPerPlayer.append(df)

    return numberOfTourneysPerPlayer.sort_values(by=['number_of_tourneys'], ascending=False).head(n)



matches2018df = pd.read_csv('data/atp_matches_2018.csv')
topPlayersWithDifferentTourney2018 = get_number_of_tourneys_per_player(matches2018df, 10)
topPlayersWithDifferentTourney2018.to_csv('data/HC_top_10_players_with_different_tourneys_2018.csv')

matches2019df = pd.read_csv('data/atp_matches_2019.csv')
topPlayersWithDifferentTourney2019 = get_number_of_tourneys_per_player(matches2019df, 10)
topPlayersWithDifferentTourney2019.to_csv('data/HC_top_10_players_with_different_tourneys_2019.csv')

matches2020df = pd.read_csv('data/atp_matches_2020.csv')
topPlayersWithDifferentTourney2020 = get_number_of_tourneys_per_player(matches2020df, 10)
topPlayersWithDifferentTourney2020.to_csv('data/HC_top_10_players_with_different_tourneys_2020.csv')


topPlayersMerged = pd.concat([topPlayersWithDifferentTourney2018, topPlayersWithDifferentTourney2019, topPlayersWithDifferentTourney2020]);

topPlayersGroupedPerPlayer = topPlayersMerged.groupby(by='player_id')

topPlayers = pd.DataFrame(columns=['player_id', 'number_of_tourneys'])

for player_id, numbers in topPlayersGroupedPerPlayer:
    df123 = pd.DataFrame({
        'player_id': [player_id],
        'number_of_tourneys': numbers.number_of_tourneys.sum()
    })

    topPlayers = topPlayers.append(df123)

topPlayers = topPlayers.sort_values(by=['number_of_tourneys'], ascending=False).head(10)
topPlayers.to_csv('data/HC_top_10_players_with_different_tourneys_all.csv')
