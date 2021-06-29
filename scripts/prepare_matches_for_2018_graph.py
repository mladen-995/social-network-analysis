import pandas as pd

# df2018_players = pd.read_csv('data/HC_players_2018.csv')

# df2018_players['Id'] = df2018_players['0']
# df2018_players['Label'] = df2018_players['1'] + ' ' + df2018_players['2']
# df2018_players.to_csv('data/HC_players_2018_nodes.csv')


df2018_matches = pd.read_csv('data/atp_matches_2018.csv')

dd = pd.DataFrame({
    'Source': df2018_matches['winner_id'],
    'Target': df2018_matches['loser_id']
})

dd.to_csv('data/atp_matches_2018_edges.csv')
