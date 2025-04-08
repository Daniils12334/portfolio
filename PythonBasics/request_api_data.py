import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) #https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status response codes
    # print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print(f"Failed to retrive data {response.status_code}")
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Name: {pokemon_name["name"]}")
    print(f"Id: {pokemon_name["id"]}")
    print(f"Height: {pokemon_name["height"]}")
    print(f"Weight: {pokemon_name["weight"]}")


