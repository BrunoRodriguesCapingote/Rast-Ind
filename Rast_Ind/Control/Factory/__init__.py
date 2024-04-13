from Rast_Ind.Control.Factory.Indentificacao import Indentificacao


class Factory:
    def __init__(self):
        pass

    def get_fac_indentificacao(self):
        return Indentificacao(nome='Indentificacao de Objetos', estado=1)
