
from datetime import datetime

from participantes.clutzdias.enums.tipo_transacao import TipoTransacao

class Transacao:
    valor: int
    tipo: TipoTransacao
    descricao: str
    realizada_em: datetime
    