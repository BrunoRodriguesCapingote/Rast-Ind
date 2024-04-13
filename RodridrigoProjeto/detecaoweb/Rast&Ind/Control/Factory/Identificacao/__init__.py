from Control.Factory.Processo import Processo
from Model.MdIdentificacao import MdIdentificacao
from View.VwIdentificacao import VwIdentificacao
import ultralytics


class Identificacao(Processo):
    def __init__(self, nome: str, estado: int):
        super().__init__(nome=nome, estado=estado)

    def executar(self, Model: MdIdentificacao, View: VwIdentificacao) -> None:
        Model.get_images__home(diretorio=r"")
