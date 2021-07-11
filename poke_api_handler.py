import requests


class PokeAPIHandler():
    def get_pokemon_base_experience(self, pokemon_url) -> int:
        """
        Retorna int base_experience do Pokemon.

        >>> get_pokemon_base_experience("https://pokeapi.co/api/v2/pokemon/butterfree/")
        178

        >>> get_pokemon_base_experience("https://pokeapi.co/api/v2/pokemon/12/")
        178
        """

        r = requests.get(pokemon_url)
        pokemon = r.json()
        
        return pokemon["base_experience"]
