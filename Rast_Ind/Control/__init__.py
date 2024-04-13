from Rast_Ind.Control.Factory import Factory
from Rast_Ind.Motor import Motor
from Rast_Ind.Model import Model
from Rast_Ind.View import View
from Rast_Ind.BitSet import BitSet


class Control:
    def __init__(self):
        self.motor = Motor()
        self.factory = Factory()
        self.view = View()
        self.bitset = BitSet()
        self.model = Model()
        self.pack_image = None
        self.operation: int = 0

    def ativar_rastreamento(self, operacao: int) -> None:
        self.operation = 1

    def set_image_pack(self, image_pack: list) -> None:
        self.pack_image = image_pack

    def iniciar_sistema(self):
        self.motor.add_process_to_exec(Processo=self.factory.get_fac_indentificacao(), View=self.view.get_vw_motor())
        self.bitset.__setattr__("_bit_permission", [self.factory.get_fac_indentificacao().estado])
        self.motor.exec_proces_list(VwMotor=self.view.get_vw_motor(), VwProcesso=self.view.get_vw_indentificacao(),
                                    MdProcesso=self.model.get_md_indentificacao(), BitSet=self.bitset)
