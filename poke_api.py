import requests

URl = 'https://pokeapi.co/api/v2/pokemon/'

def search_pokemon(search=' '):
    """
    Searches pokemon from the PokeAPI with the specifies search term

    param search: Name of the pokemon is mentioned in this param when the function is called.
    returns: If successfull, all the details of the mentioned pokemon will be returned.
    
    """


    search = str(search).strip().lower()
    print(f'Searching for {search}...', end='')

    params = { 
        'name' : search
        
    }

    search_url = URl + search 
    resp_msg = requests.get(search_url, params= params)

    if resp_msg.status_code == requests.codes.OK:
        print(f'Found {search}')
        return resp_msg.json()
   
    else:
        print(f'Did not find {search}')
        print(f'Status code: {resp_msg.status_code}, Error reason: {resp_msg.reason}')



