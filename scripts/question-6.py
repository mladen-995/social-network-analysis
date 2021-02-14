import pandas as pd
import numpy as np


def getTopNCountries(inputDataFrame, n, resultFileName):
    topNCountries = inputDataFrame['5'].value_counts().head(n)
    resultDf = pd.DataFrame({
        'country_code': topNCountries.index,
        'number_of_players': topNCountries.values
    })

    resultDf.to_csv(resultFileName)

    return resultDf


df2018 = pd.read_csv('./data/HC_players_2018.csv');
topCountriesFor2018 = getTopNCountries(df2018, 10, './data/HC_top_countries_for_2018.csv')

df2019 = pd.read_csv('./data/HC_players_2019.csv');
topCountriesFor2019 = getTopNCountries(df2019, 10, './data/HC_top_countries_for_2019.csv')

df2020 = pd.read_csv('./data/HC_players_2020.csv');
topCountriesFor2020 = getTopNCountries(df2020, 10, './data/HC_top_countries_for_2020.csv')


dfAll = pd.concat([df2018, df2019, df2020])
topCountries = getTopNCountries(dfAll, 10, './data/HC_top_countries_all.csv')
