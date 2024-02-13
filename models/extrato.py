
from typing import List
from models.saldo import Saldo
from models.transacao import Transacao

class Extrato:
    saldo: Saldo
    ultimas_transacoes: List[Transacao]