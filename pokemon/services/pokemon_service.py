import requests
from pokemon.models import Pokemon

API_URL = "https://pokeapi.co/api/v2/pokemon"

def get_all_pokemons():
    
    pokemons = []
    limit = 100    
    offset = 0

    while True:
        response = requests.get(f"{API_URL}?limit={limit}&offset={offset}")
        if response.status_code != 200:
            print(f"Error al obtener Pokémon: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])
        if not results:
            break 

        pokemons.extend(results)
        offset += limit
        print(f"Traídos hasta Pokémon {offset}")

    print(f"Total Pokémon encontrados en la API: {len(pokemons)}")
    return pokemons


def load_pokemons():
    """
    Guarda o actualiza todos los Pokémon en la base de datos.
    """
    lista = get_all_pokemons()
    total_guardados = 0

    for item in lista:
        detalle = requests.get(item["url"]).json()

        types = [t["type"]["name"] for t in detalle.get("types", [])]
        abilities = [a["ability"]["name"] for a in detalle.get("abilities", [])]

        Pokemon.objects.update_or_create(
            name=detalle["name"], 
            defaults={
                "image": detalle["sprites"]["front_default"],
                "hp": detalle["stats"][0]["base_stat"],
                "attack": detalle["stats"][1]["base_stat"],
                "height": detalle["height"],
                "weight": detalle["weight"],
                "base_experience": detalle["base_experience"],
                "types": ", ".join(types),
                "abilities": ", ".join(abilities),
            }
        )

        total_guardados += 1
        if total_guardados % 50 == 0:
            print(f"Guardados {total_guardados} Pokémon hasta ahora...")

    print(f"¡Carga completada! Total guardados o actualizados: {total_guardados}")
    return total_guardados