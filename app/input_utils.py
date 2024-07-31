import logging

input_logger = logging.getLogger('input_logger')
input_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app/logs/input.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
input_logger.addHandler(file_handler)

input_logger.propagate = False


def obter_valor_input(mensagem: str) -> float:
    """Obtém um valor numérico do usuário."""
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            input_logger.info(f'Entrada recebida: {valor:.2f}')
            return valor
        except ValueError:
            input_logger.warning(f'Entrada inválida recebida: {entrada}')
            print("Por favor, insira um valor numérico válido.")
