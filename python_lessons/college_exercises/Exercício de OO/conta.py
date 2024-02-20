""" 
Crie um arquivo chamado conta.py para representar a classe conta bancária com os seguintes atributos e métodos:

Atributos:
Número
Titular
Saldo
Limite

Métodos:

Deposita
  Para depositar dinheiro na conta. Esse método deve receber uma referência do próprio objeto e o valor a ser adicionado ao saldo da conta

Extrato
  Que recebe como argumento uma referência do próprio objeto e imprime o histórico de operações realizados na conta: saques e depósitos.

Saca
  Que realiza retiradas de dinheiro de uma conta com e retornar um valor que representa se a operação foi ou não bem-sucedida. Lembre-se que não é permitido sacar um valor maior do que o saldo.

TransferePara
  Que recebe como argumento uma referência do próprio objeto, uma Conta destino e o valor a ser transferido. Esse método deve sacar o valor do próprio objeto e depositar na conta destino.

"""
from historico import Historico

class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        if (valor < 0):
            print("Valor inválido!")
        else:
          self.saldo += valor
          self.historico.registrar_transacao(f"Depósito de {valor}")
          print("Deposito efetuado com sucesso!")

    def extrato(self):
        print(f"Extrato da conta {self.numero}:")
        self.historico.imprimir_transacoes()
        print(f"Saldo atual: {self.saldo}")
    
    def saca(self, valor):
        if(valor > self.saldo):
            print("Saldo insuficiente!")
        elif(valor < 0):
            print("Valor inválido!")
        else:
            self.saldo -= valor
            self.historico.registrar_transacao(f"Saque de {valor}")

    def transfere_para(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)
        self.historico.registrar_transacao(f"Transferência para conta {destino.numero} no valor de {valor}")
        print("Transferência realizada com sucesso!")