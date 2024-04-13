class Motor:
    def __init__(self):
        self.process_list = list()

    def exec_proces_list(self, BitSet, VwMotor, VwProcesso, MdProcesso) -> None:
        VwMotor.iniciar_execucao()
        for pos, pos_value in enumerate(BitSet):
            if pos_value == 1:
                VwMotor.permitido_execucao(Processo=self.process_list[pos])
                self.process_list[pos].executar(View=VwProcesso, Model=MdProcesso)
            elif pos_value == 0:
                VwMotor.negada_execucao(Processo=self.process_list[pos])

    def add_process_to_exec(self, Processo, View) -> None:
        View.adicionar_processo(process_name=Processo.nome)
        self.process_list.append(Processo)
        View.mostrar_processos(process_list=self.process_list)

