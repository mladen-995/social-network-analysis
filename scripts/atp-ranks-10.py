import pandas as pd

df = pd.read_csv('./data/atp_rankings_10s.csv')

def isNaN(num):
    return num != num

def formatMiddleName(name) :
    if isNaN(name) or name == 'A':
        return 'U';
    else:
        return name;



# print(df['points'].isnull().values.any())

# Format name
# df[1] = df[1].str.strip().str.upper()
# df[2] = df[2].str.strip().str.upper()

# # Format dominant hand
# df[3] = df[3].apply(formatMiddleName)


# df.to_csv('./data/atp_players_format.csv');


# print(df[5].dtype)

print(df.loc[df.points.isnull()])
