import pandas as pd

region_replacements = {
    'Zhambyl Region': 'Jambyl Region',
    'Zhetysu Region': 'Jetisu Region',
    'Abay Region': 'Abai Region',
    'Turkestan Region': 'Turkistan Region',
    'Туркестанская ':'Turkistan Region',
    'The Republic of Kazakhstan': 'The Republic Of Kazakhstan',
    'Shymkent City': 'Shymkent city',
    'Almaty City': 'Almaty city',
    'Astana City': 'Astana city',
    'The Republic Kazakhstan': 'The Republic Of Kazakhstan',
    'Область Абай': 'Abai Region',
    'Ulytau Region Region': 'Ulytau Region',
    'Актюбинская ': 'Aktobe Region',
    'Zhetisu Region': 'Jetisu Region',
    'Karagandy Region': 'Karaganda Region',
    'Astana city Region': 'Astana city'
}

df1 = pd.read_csv('./data/output.csv')
print(df1)
df1.rename(columns={'Value': 'clearance-rate'}, inplace=True)


df2 = pd.read_csv('./data/city-crime.csv')
df2.rename(columns={'Value': 'crime-rate'}, inplace=True)
print(df2)

df2['Region'] = df2['Region'].replace(region_replacements)
df1['Region'] = df1['Region'].replace(region_replacements)

df3 = pd.merge(df1,df2, on='Region', how='outer')

df3['clearance-rate-divided'] = (df3['clearance-rate']/df3['crime-rate'])

print(df3)

df3.to_csv('./data/clearance-rate-divided.csv')