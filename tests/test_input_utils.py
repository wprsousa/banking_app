import logging
import unittest
from unittest.mock import patch
from app.input_utils import obter_valor_input


class TestInputUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    @patch('builtins.input', side_effect=['abc', '123'])
    def test_obter_valor_input_invalido(self, mock_input):
        valor = obter_valor_input("Informe um valor: ")
        self.assertEqual(valor, 123.0)

    @patch('builtins.input', side_effect=['123'])
    def test_obter_valor_input_valido(self, mock_input):
        valor = obter_valor_input("Informe um valor: ")
        self.assertEqual(valor, 123.0)


if __name__ == '__main__':
    unittest.main()
