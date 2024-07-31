# Conta Bancária

Este projeto simula um sistema de conta bancária simples, desenvolvido como parte de um processo de seletivo para Engenheiro de Software Junior. O sistema permite operações básicas como depósito, saque e transferência entre contas.

## Funcionalidades

- Criação de contas bancárias com saldo inicial.
- Depósito de valores em uma conta.
- Saque de valores de uma conta.
- Transferência de valores entre contas.
- Registro de todas as transações e entradas do usuário em arquivos de log.

## Requisitos

- Python 3.6 ou superior.

## Configuração

1. Clone o repositório para sua máquina local:

    ```sh
    git clone https://github.com/wprsousa/banking_app.git
    cd banking_app
    ```

2. Instale as dependências necessárias (se houver):

    ```sh
    pip install -r requirements.txt
    ```

## Estrutura do Projeto

- **account.py**: Implementação da classe ContaBancaria
- **input_utils.py**: Funções utilitárias para entrada de dados do usuário
- **app.py**: Lógica principal do aplicativo bancário
- **test_account.py**: Testes unitários para a classe ContaBancaria
- **transactions.log**: Arquivo de log para transações bancárias (gerado automaticamente)
- **input.log**: Arquivo de log para entradas do usuário (gerado automaticamente)
- **README.md**: Este arquivo

## Uso

Para executar o aplicativo bancário, siga os passos abaixo:

1. Execute o script `app.py`:

    ```sh
    python app.py
    ```

2. Siga as instruções no console para interagir com o sistema bancário.

## Logs

- As transações bancárias são registradas no arquivo `transactions.log`.
- As entradas do usuário são registradas no arquivo `input.log`.

## Testes

Para executar os testes unitários, utilize o comando abaixo:

```sh
python test_account.py
```

Os testes verificam a funcionalidade das operações de depósito, saque e transferência, assegurando que o sistema se comporte conforme o esperado.


## Contato

Para dúvidas ou mais informações sobre o projeto, entre em contato:

- Nome: Wellington Pedro Ranha de Sousa
- Email: wprsousa@gmail.com