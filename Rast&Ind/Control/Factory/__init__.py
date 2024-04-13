from Control.Factory.Identificacao import Identificacao


class Factory:
    def __init__(self):
        pass

    def get_indentificacao(self) -> Identificacao:
        return Identificacao(nome='Identificação De Objeto', estado=1)
