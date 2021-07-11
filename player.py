class Player():
    def __init__(self, pokemon_list, max_limit_pokemons=6) -> None:
        if not pokemon_list:
            raise ValueError("Empty Pokemon list is not allowed!")
        elif type(pokemon_list) is not list:
            raise TypeError("Arg needs to be list.")
        elif len(pokemon_list) > max_limit_pokemons:
            raise ValueError("List needs to be less or equals to max_limit_pokemons arg!")

        # Lista com pokemons que o usuario escolheu trocar
        self._pokemons = pokemon_list
        # Regra de quantidade maxima de pokemons por jogador
        self._max_limit_pokemons = max_limit_pokemons


    @property
    def pokemons(self) -> list:
        """Lista de Pokemons que o usuario escolheu"""
        return self._pokemons
