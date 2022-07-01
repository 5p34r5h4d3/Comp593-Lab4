from sys import argv
from poke_api import search_pokemon
from pastebin import post_new_paste


def main():

    search = argv[1]
    pokedex = search_pokemon(search)

    if pokedex:

        paste_title = get_paste_title(search)

        paste_body = get_paste_body(pokedex)

        paste_url = post_new_paste(paste_title, paste_body, '10M')

        print(paste_url)

def get_paste_body(pokedex):

    ability_list = [i['ability']['name'] for i in pokedex['abilities']]
    paste_body = '\n- '.join(ability_list)
    p_body = str(f'- {paste_body}')
    return p_body
  
def get_paste_title(search):
    return f'{search.capitalize()}\'s Abilities'

main()
   


