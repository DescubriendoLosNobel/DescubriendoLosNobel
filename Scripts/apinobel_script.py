import requests
import json

def get_nobel_laureates(params=None):
    url = 'https://api.nobelprize.org/2.1/laureates'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        return None

def get_nobel_prizes(params=None):
    url = 'https://api.nobelprize.org/2.1/nobelPrizes'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        return None

# Ejemplo de uso:
# Obtener laureados con filtros específicos
laureate_params = {
    'gender': 'female',
    'nobelPrize': 'pea',
    'birthCountry': 'Poland'
}
laureates_data = get_nobel_laureates(laureate_params)
print(json.dumps(laureates_data, indent=4))

# # Obtener premios Nobel con filtros específicos
# prize_params = {
#     'nobelPrize': 'lit',
#     'awardYear': '2020'
# }
# prizes_data = get_nobel_prizes(prize_params)
# print(json.dumps(prizes_data, indent=4))
