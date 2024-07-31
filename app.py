from account import ContaBancaria
from input_utils import obter_valor_input
import logging

logging.basicConfig(filename='transactions.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main() -> None:
    logging.info('Iniciando o aplicativo')

    conta1_saldo_inicial = obter_valor_input("Informe o saldo inicial da Conta 1: R$")
    conta2_saldo_inicial = obter_valor_input("Informe o saldo inicial da Conta 2: R$")

    conta1 = ContaBancaria(conta1_saldo_inicial)
    conta2 = ContaBancaria(conta2_saldo_inicial)

    logging.info(f"Saldo inicial da Conta 1: R${conta1_saldo_inicial:.2f}")
    logging.info(f"Saldo inicial da Conta 2: R${conta2_saldo_inicial:.2f}")

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")
        logging.info(f'Opção escolhida: {escolha}')

        if escolha == "1":
            valor_deposito = obter_valor_input("Informe o valor a ser depositado na Conta 1: R$")
            conta1.depositar(valor_deposito)
        elif escolha == "2":
            valor_saque = obter_valor_input("Informe o valor a ser sacado da Conta 1: R$")
            conta1.sacar(valor_saque)
        elif escolha == "3":
            valor_transferencia = obter_valor_input("Informe o valor a ser transferido da Conta 1 para a Conta 2: R$")
            conta1.transferir(conta2, valor_transferencia)
        elif escolha == "4":
            logging.info('Encerrando o aplicativo bancário')
            break
        else:
            print("Opção inválida. Tente novamente.")
            logging.warning(f'Opção inválida escolhida: {escolha}')

    print("\nSaldos Finais:")
    print(f"Conta 1: R${conta1.saldo:.2f}")
    print(f"Conta 2: R${conta2.saldo:.2f}")


if __name__ == "__main__":
    main()
