from player import Player

from math import isclose


class TradeCalculator():
    def __init__(self, player1, player2) -> None:
        self._player1 = player1
        self._player2 = player2


    def is_trade_valid(self) -> bool:
        """Define se a instancia de TradeCalculator gera um trade valido"""
        base_experience_player1 = self._total_base_experience(self._player1)
        base_experience_player2 = self._total_base_experience(self._player2)

        is_trade_valid = self._is_base_experience_approximated(base_experience_player1, base_experience_player2)

        return is_trade_valid


    def _total_base_experience(self, player: Player) -> int:
        """Calcula soma total de base_experience dos pokemons do player"""
        if type(player) is not Player:
            raise TypeError("Arg type needs to be Player object.")

        # Generator para somar a base_experience de todos os pokemons escolhidos
        total_base_experience = sum(pokemon.base_experience for pokemon in player.pokemons)

        return total_base_experience


    def _is_base_experience_approximated(self, total_base_exp_player1: int, total_base_exp_player2: int) -> bool:
        """Recebe a soma de base_experience de dois players
        Verifica se as somas de base_experience de cada player esta aproximada

        A aproximacao eh feita usando uma tolerancia de 2 pontos
        """

        if (type(total_base_exp_player1) is not int) or (type(total_base_exp_player2) is not int):
            raise TypeError("Args needs to be of integer type.")
        elif (total_base_exp_player1 < 0 or total_base_exp_player2 < 0) or (total_base_exp_player1 == 0 or total_base_exp_player2 == 0):
            raise ValueError("Args needs to be positive value.")

        # Retorna aproximacao, usando tolerancia absoluta de 2 pontos para cima ou para baixo.
        return isclose(total_base_exp_player1, total_base_exp_player2, abs_tol=2)
