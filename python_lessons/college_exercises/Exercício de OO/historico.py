"""
Crie uma classe Histórico (histórico.py) que represente o histórico de uma Conta exibindo a sequência de saldo, saque e depósito. Faça testes no console do Python criando algumas contas, fazendo operações e por último mostrando o histórico de transações de uma Conta.

"""

class Historico:
    def __init__(self):
        self.transacoes = []

    def registrar_transacao(self, descricao):
        self.transacoes.append(descricao)

    def imprimir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao)