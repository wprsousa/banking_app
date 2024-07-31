import logging

logging.basicConfig(
    filename='app/logs/transactions.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class ContaBancaria:
    def __init__(self, saldo_inicial: float = 0.0):
        """Inicializa uma nova conta bancária com um saldo inicial."""
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        """Deposita um valor na conta."""
        if valor > 0:
            saldo_anterior = self.saldo
            self.saldo += valor
            self._imprimir_transacao("Depósito", valor)
            logging.info(
                f"Saldo anterior: R${saldo_anterior:.2f}. Depósito de R${valor:.2f} realizado. "
                f"Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito. Depósito não realizado")
            logging.warning(f'Tentativa de depósito de valor inválido: R${valor:.2f}.')

    def sacar(self, valor: float) -> None:
        """Saca um valor da conta se houver saldo suficiente."""
        if valor <= 0:
            print("Valor inválido para saque. Saque não realizada.")
            logging.warning(f'Tentativa de saque de valor inválido: R${valor:.2f}.')
        elif valor <= self.saldo:
            saldo_anterior = self.saldo
            self.saldo -= valor
            self._imprimir_transacao("Saque", valor)
            logging.info(f"Saldo anterior: {saldo_anterior:.2f}. Saque de R${valor:.2f} realizado. "
                         f"Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente. Operação não realizada.")
            logging.warning(f'Tentativa de saque de R${valor:.2f} falhou. Saldo insuficiente.')

    def transferir(self, destinatario: 'ContaBancaria', valor: float) -> None:
        """Transfere um valor para outra conta bancária se houver saldo suficiente e o valor for positivo."""
        if valor > 0:
            if valor <= self.saldo:
                saldo_anterior = self.saldo
                self.saldo -= valor
                destinatario.depositar(valor)
                self._imprimir_transacao("Transferência", valor)
                logging.info(f"Saldo anterior: R${saldo_anterior:.2f}. Transferência de R${valor:.2f} realizada. "
                             f"Novo saldo: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente. Transferência não realizada.")
                logging.warning(f'Tentativa de transfêrencia de R${valor:.2f} falhou. Saldo insuficiente.')
        else:
            print("Valor inválido para transferência. Transferência não realizada.")
            logging.warning(f'Tentativa de transferência de valor inválido: R${valor:.2f}.')

    def _imprimir_transacao(self, tipo_transacao: str, valor: float) -> None:
        """Imprime os detalhes da transação"""
        print(f"{tipo_transacao} de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
