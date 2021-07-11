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

        self.assertRaises(ValueError, Player([Pokemon("Pichu", APIHandler.get_base_experience("Pichu")), Pokemon("Pikachu", APIHandler.get_base_experience("Pikachu"))], max_limit_pokemons=1), "Lista de Pokemons ultrapassou o limite.")


if __name__ == "__main__":
    unittest.main()
