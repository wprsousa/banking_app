import unittest
import logging
from app.account import ContaBancaria


class TestContaBancaria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.disable(logging.CRITICAL)

    @classmethod
    def tearDownClass(cls):
        logging.disable(logging.NOTSET)

    def setUp(self):
        self.conta1 = ContaBancaria(100)
        self.conta2 = ContaBancaria(50)

    def test_depositar(self):
        self.conta1.depositar(50)
        self.assertEqual(self.conta1.saldo, 150)

    def test_depositar_valor_negativo(self):
        self.conta1.depositar(-50)
        self.assertEqual(self.conta1.saldo, 100)
        self.assertEqual(self.conta2.saldo, 50)

    def test_sacar_com_saldo_suficiente(self):
        self.conta1.sacar(50)
        self.assertEqual(self.conta1.saldo, 50)

    def test_sacar_com_saldo_insuficiente(self):
        self.conta1.sacar(150)
        self.assertEqual(self.conta1.saldo, 100)

    def test_sacar_valor_negativo(self):
        self.conta1.sacar(-50)
        self.assertEqual(self.conta1.saldo, 100)
        self.assertEqual(self.conta2.saldo, 50)

    def test_transferir_com_saldo_suficiente(self):
        self.conta1.transferir(self.conta2, 50)
        self.assertEqual(self.conta1.saldo, 50)
        self.assertEqual(self.conta2.saldo, 100)

    def test_transferir_com_saldo_insuficiente(self):
        self.conta1.transferir(self.conta2, 150)
        self.assertEqual(self.conta1.saldo, 100)
        self.assertEqual(self.conta2.saldo, 50)

    def test_transferir_valor_invalido(self):
        self.conta1.transferir(self.conta2, -50)
        self.assertEqual(self.conta1.saldo, 100)
        self.assertEqual(self.conta2.saldo, 50)


if __name__ == '__main__':
    unittest.main()
