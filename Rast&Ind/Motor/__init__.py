from BitSet import BitSet


class Motor:
    def __init__(self):
        self.lista_de_processos = list()

    def exec_process_list(self, BitSet, MdProcesso, VwMotor, VwProcesso) -> None:
        VwMotor.iniciando_execucao(process_list=self.lista_de_processos)
        for x, pos in enumerate(BitSet):
            if BitSet[x] == 1:
                VwMotor.execucao_aceita(Processo=self.lista_de_processos[x])
                self.lista_de_processos[x].executar(Model=MdProcesso, View=VwProcesso)

    def add_process_to_exec(self, Processo, View) -> None:
        View.adicionar_processo(process_name=Processo.nome)
        self.lista_de_processos.append(Processo)
        View.mostrar_processos(process_list=self.lista_de_processos)
