from View.VwIdentificacao import VwIdentificacao
from View.VwMotor import VwMotor


class View:
    def __init__(self):
        pass

    def get_vw_motor(self) -> VwMotor:
        return VwMotor()

    def get_vw_indentificacao(self) -> VwIdentificacao:
        return VwIdentificacao()
