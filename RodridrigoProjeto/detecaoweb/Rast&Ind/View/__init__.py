from View.VwIndenificacao import VwIndentificacao
from View.VwMotor import VwMotor


class View:
    def __init__(self):
        pass

    def get_vw_indentificacao(self):
        return VwIndentificacao()

    def get_vw_motor(self):
        return VwMotor()
