import pandas as pd
import requests

r = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
response = r.json()
df = pd.DataFrame.from_dict(response['cand'])
df = df[['nm', 'vap', 'pvap']]
print(df)
