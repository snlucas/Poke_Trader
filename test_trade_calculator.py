from pokemon import Pokemon
from player import Player
from trade_calculator import TradeCalculator

import unittest


class TestTradeCalculator(unittest.TestCase):
    def test_player_total_base_experience_passing_wrong_type(self):
        """Teste passando argumento diferente de Player
        
        >>> _total_base_experience(Player(...))
        sum(Player(Pokemon.base_experience, ...))

        >>> _total_base_experience(wrong_type)
        Error
        """

        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 260)])
        tc = TradeCalculator(p1, p2)
        self.assertRaises(TypeError, lambda: tc._total_base_experience(42))        


    def test_is_trade_valid_returns_True(self):
        """Teste para trade valido
        
        >>> tc = TradeCalculator(Player(...), Player(...))
        >>> tc.is_trade_valid()
        True
        """

        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 155)])
        tc = TradeCalculator(p1, p2)
        self.assertTrue(tc.is_trade_valid(), "Funcao nao esta retornando o valor correto.")


    def test_is_trade_valid_returns_False(self):
        """Teste para trade invalido

        >>> tc = TradeCalculator(Player(...), Player(...))
        >>> tc.is_trade_valid()
        False
        """
        
        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 260)])
        tc = TradeCalculator(p1, p2)
        self.assertRaises(TypeError, lambda: tc.is_trade_valid(42))


    def test_is_base_experience_approximated_passing_wrong_type(self):
        """Teste passando argumentos diferentes de inteiro
        
        >>> _is_base_experience_approximated(42, 42)
        bool

        >>> _is_base_experience_approximated([...])
        Error
        """
        
        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 260)])
        tc = TradeCalculator(p1, p2)
        self.assertRaises(TypeError, lambda: tc._is_base_experience_approximated({'n1': 42}, {'n2': 13}))


    def test_is_base_experience_approximated_passing_negative_value(self):
        """Teste passando um argumento negativo
        
        >>> _is_base_experience_approximated(42, 42)
        bool

        >>> _is_base_experience_approximated(-10, 4)
        Error
        """

        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 260)])
        tc = TradeCalculator(p1, p2)
        self.assertRaises(ValueError, lambda: tc._is_base_experience_approximated(-42, 10))


    def test_is_base_experience_approximated_passing_zero_value(self):
        """Teste passando um argumento nulo
        
        >>> _is_base_experience_approximated(42, 42)
        bool

        >>> _is_base_experience_approximated(0, 4)
        Error
        """

        p1 = Player([Pokemon("Pichu", 42), Pokemon("Pikachu", 145)])
        p2 = Player([Pokemon("Dito", 30), Pokemon("Charizard", 260)])
        tc = TradeCalculator(p1, p2)
        self.assertRaises(ValueError, lambda: tc._is_base_experience_approximated(0, 10))


if __name__ == "__main__":
    unittest.main()
