from Control.Factory import Factory
from Motor import Motor
from Model import Model
from View import View
from BitSet import BitSet


class Control:
    def __init__(self):
        self.motor = Motor()
        self.factory = Factory()
        self.view = View()
        self.bitset = BitSet()
        self.model = Model()

    def iniciar_sistema(self):
        self.motor.add_process_to_exec(Processo=self.factory.get_fac_indentificacao(), View=self.view.get_vw_motor())
        self.bitset.__setattr__("_bit_permission",[self.factory.get_fac_indentificacao().estado])
        self.motor.exec_proces_list(VwMotor=self.view.get_vw_motor(), VwProcesso=self.view.get_vw_indentificacao(),MdProcesso=self.model.get_md_indentificacao(), BitSet=self.bitset)


if __name__ == "__main__":
    crt = Control()
    crt.iniciar_sistema()
