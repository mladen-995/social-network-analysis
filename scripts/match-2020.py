import pandas as pd

df = pd.read_csv('./data/atp_matches_2020.csv')

def isNaN(num):
    return num != num

def formatMiddleName(name) :
    if isNaN(name) or name == 'A':
        return 'U';
    else:
        return name;


# print(df[df.duplicated(['tourney_id', 'match_num'])])

print(df.loc[df.loser_id.isnull()])



# print(df[df.duplicated(subset=['tourney_id','match_num'], keep=False)])
# re = df.groupby(['tourney_id', 'match_num']).size().rename('FF')
# re = df.groupby(['tourney_id'])
# print(re.FF != 1)


# column_values = df[["tourney_id", "match_num"]].values
# unique_values =  pd.unique(column_values)

# print(df['tourney_id'].is_unique)


# print(df['points'].isnull().values.any())

# Format name
# df[1] = df[1].str.strip().str.upper()
# df[2] = df[2].str.strip().str.upper()

# # Format dominant hand
# df[3] = df[3].apply(formatMiddleName)


# df.to_csv('./data/atp_players_format.csv');


# print(df[5].dtype)

# print(df.loc[df.points.isnull()])
