from player import Player
from pokemon import Pokemon
import unittest


class TestPlayer(unittest.TestCase):
    def test_create_player_obj_with_empty_pokemon_list(self):
        """Testa instancia de classe usando uma lista vazia."""
        self.assertRaises(ValueError, lambda: Player([]))


    def test_create_player_obj_with_non_list_type_pokemons(self):
        """Testa instancia de classe, usando um tipo diferente do esperado."""
        self.assertRaises(TypeError, lambda: Player({"pokemon1": "charmander", "pokemon2": "pikachu", "pokemon3": "pichu"}))


    def test_create_player_obj_with_more_than_max_pokemons(self):
        """Testa instancia de classe usando uma lista com mais Pokemons do que ela esta definida para ter."""
        from poke_api_handler import PokeAPIHandler

        # Teste usando a url do Pokemon Butterfree
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/butterfree/"
        poke_api_handler = PokeAPIHandler()  # A classe precisa ser instanciada antes da chamada de um metodo
        base_experience = poke_api_handler.get_pokemon_base_experience(pokemon_url)

        self.assertRaises(ValueError, lambda: Player([Pokemon("Pichu", base_experience), Pokemon("Pikachu", base_experience)], max_limit_pokemons=1))


if __name__ == "__main__":
    unittest.main()
