from sys import argv
from pokebase import pokemon
from poke_api import search_pokemon
from pastebin import post_new_paste
from requests import get
from PIL import Image
from io import BytesIO


def main():

    search = argv[1]
    search = str(search).strip().lower()
    pokedex = search_pokemon(search)
    poke = pokemon(search)
    pic = get(poke.sprites.front_default).content

    if pokedex:

        paste_title = get_paste_title(search)

        paste_body = get_paste_body(pokedex)

        paste_url = post_new_paste(paste_title, paste_body, '10M')

        print(paste_url)

        
        image = Image.open(BytesIO(pic))
        image.show()
        

        
def get_paste_body(pokedex):

    ability_list = [i['ability']['name'] for i in pokedex['abilities']] 
    paste_body = '\n- '.join(ability_list)
    p_body = str(f'- {paste_body}')
    return p_body
  
def get_paste_title(search):
    return f'{search.capitalize()}\'s Abilities'



main()
   


