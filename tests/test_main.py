import unittest
import logging
from unittest.mock import patch
from app.account import ContaBancaria
from app.main import iniciar_saldo_conta, processa_escolha, log_opcao_escolhida


class TestBankingApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    @patch('builtins.input', side_effect=['100.0', '200.0'])
    def test_iniciar_saldo_conta(self, mock_input):
        conta1, conta2 = iniciar_saldo_conta()
        self.assertEqual(conta1.saldo, 100.0)
        self.assertEqual(conta2.saldo, 200.0)

    @patch('builtins.input', side_effect=['1', '100.0', '2', '50.0', '3', '20.0', '4'])
    @patch('app.input_utils.obter_valor_input', side_effect=[100.0, 200.0, 100.0, 50.0, 20.0])
    def test_main(self, mock_obter_valor_input, mock_input):
        with patch('logging.info') as mock_logging_info, patch('logging.warning') as mock_logging_warning:
            from app.main import main  # Importa main dentro do teste para garantir que o mock funcione
            main()
            mock_logging_info.assert_called()
            # Verifique apenas warnings específicos
            self.assertEqual(mock_logging_warning.call_count, 2)
            mock_logging_warning.assert_any_call('Tentativa de saque de R$50.00 falhou. Saldo insuficiente.')
            mock_logging_warning.assert_any_call('Tentativa de transferência de R$20.00 falhou. Saldo insuficiente.')

    @patch('builtins.input', return_value='50.0')
    @patch('app.input_utils.obter_valor_input', return_value=50.0)
    def test_processa_escolha_depositar(self, mock_obter_valor_input, mock_input):
        conta1 = ContaBancaria(100.0)
        conta2 = ContaBancaria(200.0)
        self.assertTrue(processa_escolha('1', conta1, conta2))
        self.assertEqual(conta1.saldo, 150.0)

    @patch('builtins.input', return_value='50.0')
    @patch('app.input_utils.obter_valor_input', return_value=50.0)
    def test_processa_escolha_sacar(self, mock_obter_valor_input, mock_input):
        conta1 = ContaBancaria(100.0)
        conta2 = ContaBancaria(200.0)
        self.assertTrue(processa_escolha('2', conta1, conta2))
        self.assertEqual(conta1.saldo, 50.0)

    @patch('builtins.input', return_value='50.0')
    @patch('app.input_utils.obter_valor_input', return_value=50.0)
    def test_processa_escolha_transferir(self, mock_obter_valor_input, mock_input):
        conta1 = ContaBancaria(100.0)
        conta2 = ContaBancaria(200.0)
        self.assertTrue(processa_escolha('3', conta1, conta2))
        self.assertEqual(conta1.saldo, 50.0)
        self.assertEqual(conta2.saldo, 250.0)

    @patch('builtins.input', return_value='4')
    def test_processa_escolha_sair(self, mock_input):
        conta1 = ContaBancaria(100.0)
        conta2 = ContaBancaria(200.0)
        self.assertFalse(processa_escolha('4', conta1, conta2))

    def test_log_opcao_escolhida(self):
        with patch('logging.info') as mock_logging_info:
            log_opcao_escolhida('1', 'depositar')
            mock_logging_info.assert_called_with('Opção escolhida: 1 - Depositar')


if __name__ == '__main__':
    unittest.main()
