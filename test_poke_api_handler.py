from poke_api_handler import PokeAPIHandler

import unittest
import requests


class TestPokeAPIHandler(unittest.TestCase):
    def test_api_connection_return_status_code_ok(self):
        """Testa se o status code da API retorna 200 "OK"."""

        r = requests.get("https://pokeapi.co/api/v2/pokemon/1")
        self.assertEqual(200, r.status_code, "API status is not as expected.")


    def test_get_pokemon_base_experience_returns_int(self):
        """Testa se a base_experience esta retornando um inteiro"""

        pokemon_url = "https://pokeapi.co/api/v2/pokemon/butterfree"
        r = requests.get(pokemon_url)
        pokemon = r.json()
        base_experience = pokemon["base_experience"]

        self.assertEqual(type(base_experience), int, "Tipo retornado diferente do esperado.")


    def test_get_pokemon_base_experience_returns_positive_value(self):
        """Testa se a base_experience retornada eh positiva."""

        pokemon_url = "https://pokeapi.co/api/v2/pokemon/butterfree"
        r = requests.get(pokemon_url)
        pokemon = r.json()
        base_experience = pokemon["base_experience"]

        self.assertGreaterEqual(base_experience, 0, "Valor negativo retornado.")


if __name__ == "__main__":
    unittest.main()
