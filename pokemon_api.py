import json

import requests
import pandas as pd
import ast


class Pokemon():
    base_api = 'https://pokeapi.co/api/v2'

    def __init__(self):
        self.pokemon_list = []

    def buscar_pokemon(self):
        pokemon_name = str(input('Nome do Pokemon: '))

        api = f'{self.base_api}/pokemon/{pokemon_name}'
        payload = requests.get(api).json()

        abilities = [ability['ability']['name'] for ability in payload['abilities']]
        types = [pokemon_type['type']['name'] for pokemon_type in payload['types']]

        api = f'{self.base_api}/pokemon-species/{pokemon_name}'
        payload = requests.get(api).json()

        color = payload['color']['name']
        habit = payload['habitat']['name']
        shape = payload['shape']['name']

        pokemon_dict = {
            "nome": pokemon_name,
            "cor": color,
            "habitat": habit,
            "tipo": types,
            "habilidades": abilities,
            "forma": shape
        }

        # self.pokemon_list.append(pokemon_dict)

        pokemon_table = pd.DataFrame(pokemon_dict, columns=["nome", "cor", "tipo", "forma"])

        return pokemon_table


busca = Pokemon()
print(busca.buscar_pokemon())