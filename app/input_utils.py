import logging
import os


def configurar_logger(logger_name, filename):
    """Configura o arquivo de log para salvar mensagens em um arquivo específico."""
    log_directory = '/Users/wellingtonpedro/Documents/Processo Seletivo Itau/Python/banking_app/app/logs'
    log_path = os.path.join(log_directory, filename)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False

    return logger


input_logger = configurar_logger('input_logger', 'input.log')


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
