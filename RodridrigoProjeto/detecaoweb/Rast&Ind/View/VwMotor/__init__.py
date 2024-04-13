class VwMotor:
    def __init__(self):
        self.response_name = 'Motor::Response -->> '
        self.padrao_list = list((
            "{}Adicionando processo {} a lista de execução.",
            "{}Lista de processos atual:: {}",
            "{}Iniciando execução da lista de processos.",
            "{}Permitida a execução do processo {} com estado : {}.",
            "{}Negada a execução do processo {} com estado : {}.",
        ))

    def adicionar_processo(self, process_name: str) -> None:
        print(self.padrao_list[0].format(self.response_name, process_name))

    def mostrar_processos(self, process_list: list) -> None:
        print(self.padrao_list[1].format(self.response_name, process_list))

    def iniciar_execucao(self):
        print(self.padrao_list[2].format(self.response_name))

    def permitido_execucao(self, Processo):
        print(self.padrao_list[3].format(self.response_name, Processo.nome, Processo.estado))

    def negada_execucao(self, Processo):
        print(self.padrao_list[4].format(self.response_name, Processo.nome, Processo.estado))
