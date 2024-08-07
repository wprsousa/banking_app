import logging
import os
from app.account import ContaBancaria
from app.input_utils import obter_valor_input

log_directory = '/Users/wellingtonpedro/Documents/Processo Seletivo Itau/Python/banking_app/app/logs'
log_file = os.path.join(log_directory, 'transactions.log')

logging.basicConfig(filename='app/logs/transactions.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def iniciar_saldo_conta() -> tuple:
    """Inicializa o saldo da Conta1 e da Conta2"""
    conta1_saldo_inicial = obter_valor_input('Informe o saldo inicial da Conta 1: R$')
    conta2_saldo_inicial = obter_valor_input('Informe o saldo inicial da Conta 2: R$')

    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    logging.info(f'Saldo inicial da Conta 1: R${conta1_saldo_inicial:.2f}')
    logging.info(f'Saldo inicial da Conta 2: R${conta2_saldo_inicial:.2f}')

    return conta1, conta2


def exibir_opcoes() -> None:
    """Exibe para o usuário as opções de operações bancárias disponíveis"""
    print('\nOpções:')
    print('1. Depositar')
    print('2. Sacar')
    print('3. Transferir')
    print('4. Sair')


def processa_escolha(escolha: str, conta1: ContaBancaria, conta2: ContaBancaria) -> bool:
    """Processa a escolha e executa a operação bancária correspondente"""
    try:
        if escolha == '1':
            log_opcao_escolhida(escolha, 'depositar')
            valor_deposito = obter_valor_input('Informe o valor a ser depositado na Conta 1: R$')
            conta1.depositar(valor_deposito)
        elif escolha == '2':
            log_opcao_escolhida(escolha, 'sacar')
            valor_saque = obter_valor_input('Informe o valor a ser sacado da Conta 1: R$')
            conta1.sacar(valor_saque)
        elif escolha == '3':
            log_opcao_escolhida(escolha, 'transferir')
            valor_transferencia = obter_valor_input('Informe o valor a ser transferido da Conta 1 para a Conta 2: R$')
            conta1.transferir(conta2, valor_transferencia)
        elif escolha == '4':
            log_opcao_escolhida(escolha, 'sair')
            logging.info('Encerrando o aplicativo bancário')
            return False
        else:
            print('Opção inválida. Tente novamente.')
            logging.warning(f'Opção inválida escolhida: {escolha}')
    except (ValueError, AttributeError) as e:
        logging.error(f'Erro ao processar {e}')
        print(f'Ocorreu um erro: {e}')
    return True


def exibe_saldo(conta1: ContaBancaria, conta2: ContaBancaria) -> None:
    """Exibe o saldo final da Conta 1 e da Conta 2"""
    print('\nSaldos Finais:')
    print(f'Conta 1: R${conta1.saldo:.2f}')
    print(f'Conta 2: R${conta2.saldo:.2f}')


def log_opcao_escolhida(escolha: str, tipo: str) -> None:
    """Registra o log da opção escolhida pelo usuário"""
    logging.info(f'Opção escolhida: {escolha} - {tipo.capitalize()}')


def main() -> None:
    """Função principal que inicia o aplicativo bancário, gerencia o fluxo de operações e
    exibe os saldos finais das contas."""
    logging.info('Iniciando o aplicativo')

    conta1, conta2 = iniciar_saldo_conta()

    continuar = True
    while continuar:
        exibir_opcoes()
        escolha = input('Escolha uma opção (1-4): ')
        continuar = processa_escolha(escolha, conta1, conta2)

    exibe_saldo(conta1, conta2)


if __name__ == "__main__":
    main()
