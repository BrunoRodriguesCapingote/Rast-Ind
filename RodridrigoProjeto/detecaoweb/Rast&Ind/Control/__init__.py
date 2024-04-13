from Model import Model
from Motor import Motor
from View import View
from BitSet import BitSet
from Control.Factory import Factory


class Control:
    def __init__(self) -> None:
        pass

    def iniciar_sistema(self) -> None:
        view = View()
        motor = Motor()
        model = Model()
        factory = Factory()
        bitset = BitSet()
        motor.add_process_to_exec(Processo=factory.get_indentificacao(), View=view.get_vw_motor())
        bitset.set_bit_permition(permition_list=[factory.get_indentificacao().__getattribute__("estado")])
        motor.exec_process_list(BitSet=bitset,MdProcesso=model.get_md_indentificacao(),VwMotor=view.get_vw_motor(),VwProcesso=view.get_vw_indentificacao())


if __name__ == '__main__':
    ctr = Control()
    ctr.iniciar_sistema()
