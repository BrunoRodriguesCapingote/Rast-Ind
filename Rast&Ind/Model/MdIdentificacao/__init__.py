class MdIdentificacao:
    def __it__(self):
        self.conexao = None

    def get_images__api(self) -> list:
        return list()

    def get_images__home(self, diretorio: str) -> list:
        return list()

    def set_conexao_in_api_from_host(host: str) -> None:
        pass

    def get_conexao_in_api_from_host(self):
        return self.conexao
