class VwMotor:
    def __init__(self):
        self.response_name: str = "Motor::response-->>"
        self.padrao_list = list(("{} Adicionando o processo com nome {} a lista de processos.",
                                 "{} Lista de processos : {}",
                                 "{} Iniciando a execução com a seguinte lista de processos: {}",
                                 "{} Processo :: [ {} ] :: Permissao para execução negada. Estado = {}.",
                                 "{} Processo :: [ {} ] :: Permissao para execução aceita. Estado = {}."
                                 ))

    def adicionar_processo(self, process_name: str) -> None:
        print(self.padrao_list[0].format(self.response_name, process_name))

    def mostrar_processos(self, process_list: list) -> None:
        print(self.padrao_list[1].format(self.response_name, process_list))

    def iniciando_execucao(self, process_list: list):
        print(self.padrao_list[2].format(self.response_name, process_list))

    def negar_execucao(self,Processo) -> None:
        print(self.padrao_list[3].format(self.response_name, Processo.__getattribute__("nome"), Processo.__getattribute__("estado")))

    def execucao_aceita(self,Processo) -> None:
        print(self.padrao_list[4].format(self.response_name, Processo.__getattribute__("nome"), Processo.__getattribute__("estado")))
