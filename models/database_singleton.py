class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Criando nova conexão com o banco de dados...")
            cls._instance = super().__new__(cls)
            cls._instance.connection = cls._connect()
        return cls._instance

    @staticmethod
    def _connect():
        return "Conectado ao banco de dados MySQL"

    def get_connection(self):
        return self.connection
