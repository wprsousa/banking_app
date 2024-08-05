import logging
import os


def configurar_logging(filename: str) -> None:
    """Configura o arquivo de log para salvar mensagens em um arquivo específico."""
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


log_directory = '/Users/wellingtonpedro/Documents/Processo Seletivo Itau/Python/banking_app/app/logs'
log_path = os.path.join(log_directory, 'transactions.log')
configurar_logging(log_path)


class ContaBancaria:
    def __init__(self, saldo_inicial: float = 0.0):
        """Inicializa uma nova conta bancária com um saldo inicial."""
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        """Deposita um valor na conta."""
        if valor > 0:
            saldo_anterior = self.saldo
            self.saldo += valor
            self._exibir_detalhes_transacao("Depósito", valor)
            self._log_transacao("Depósito", valor, saldo_anterior, self.saldo)
        else:
            self._exibir_detalhes_transacao_invalida("depósito")
            self._log_transacao_invalida("depósito", valor)

    def sacar(self, valor: float) -> None:
        """Saca um valor da conta se houver saldo suficiente."""
        if valor <= 0:
            self._exibir_detalhes_transacao_invalida("saldo")
            self._log_transacao_invalida("saldo", valor)
        elif valor <= self.saldo:
            saldo_anterior = self.saldo
            self.saldo -= valor
            self._exibir_detalhes_transacao("Saque", valor)
            self._log_transacao("Saque", valor, saldo_anterior, self.saldo)
        else:
            self._exibir_detalhes_transacao_saldo_insuficiente()
            self._log_transacao_saldo_insuficiente("saque", valor)

    def transferir(self, destinatario: 'ContaBancaria', valor: float) -> None:
        """Transfere um valor para outra conta bancária se houver saldo suficiente e o valor for positivo."""
        if valor > 0:
            if valor <= self.saldo:
                saldo_anterior = self.saldo
                self.saldo -= valor
                destinatario.depositar(valor)
                self._exibir_detalhes_transacao("Transferência", valor)
                self._log_transacao("Transferência", valor, saldo_anterior, self.saldo)
            else:
                self._exibir_detalhes_transacao_saldo_insuficiente()
                self._log_transacao_saldo_insuficiente("transferência", valor)
        else:
            self._exibir_detalhes_transacao_invalida("transferência")
            self._log_transacao_invalida("transferência", valor)

    def _exibir_detalhes_transacao(self, tipo_transacao: str, valor: float) -> None:
        """Exibe os detalhes de uma transação válida."""
        genero_tipo_transacao = self.identifica_sufixo_transacao(tipo_transacao.lower())
        print(f"{tipo_transacao} de R${valor:.2f} {genero_tipo_transacao}. Novo saldo: R${self.saldo:.2f}")

    @staticmethod
    def _exibir_detalhes_transacao_invalida(tipo_transacao: str) -> None:
        """Exibe os detalhes de uma transação inválida"""
        print(f"Valor inválido para {tipo_transacao}. {tipo_transacao.capitalize()} não realizado.")

    def _exibir_detalhes_transacao_saldo_insuficiente(self) -> None:
        """Exibe os detalhes de uma transação com saldo insuficiente"""
        print(f"Saldo insuficiente: R${self.saldo:.2f}. Operação não realizada.")

    def _log_transacao(self, tipo_transacao: str, valor: float, saldo_anterior: float, novo_saldo: float) -> None:
        """Loga os detalhes de uma transação válida"""
        sufixo_tipo_transacao = self.identifica_sufixo_transacao(tipo_transacao.lower())
        logging.info(
            f"{tipo_transacao} {sufixo_tipo_transacao}. Saldo anterior: R${saldo_anterior:.2f}. "
            f"{tipo_transacao.capitalize()} de R${valor:.2f} {sufixo_tipo_transacao}. "
            f"Novo saldo: R${novo_saldo:.2f}")

    @staticmethod
    def _log_transacao_invalida(tipo_transacao: str, valor) -> None:
        """Loga os detalhes de uma transação inválida"""
        logging.warning(f"Tentativa de {tipo_transacao.lower()} de valor inválido: {valor}")

    @staticmethod
    def _log_transacao_saldo_insuficiente(tipo_transacao: str, valor: float) -> None:
        """Loga os detalhes de uma transação com saldo insuficiente"""
        logging.warning(f'Tentativa de {tipo_transacao.lower()} de R${valor:.2f} falhou. Saldo insuficiente.')

    @staticmethod
    def identifica_sufixo_transacao(tipo_transacao: str) -> str:
        """Identifica o sufixo do tipo transação"""
        if tipo_transacao in ['depósito', 'saque']:
            return "realizado"
        else:
            return "realizada"
