"""
Crie um arquivo conta_teste.py e importe a classe conta (from conta import Conta) e realize os seguintes testes.

Crie duas ou mais contas
Realize depósitos, saques e transferências.
Imprima o extrato da conta.

"""

from conta import Conta

c1 = Conta(1, "Rodrigo", 100, 500)
c2 = Conta(2, "Juliano", 100, 500)

c1.deposita(100)

c1.extrato()

c1.saca(100)
c1.extrato()

c2.transfere_para(c1,100)

c1.extrato()

c2.extrato()