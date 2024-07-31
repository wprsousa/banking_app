import logging

logging.basicConfig(filename='input.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def obter_valor_input(mensagem: str) -> float:
    """Obtém um valor numérico do usuário."""
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
