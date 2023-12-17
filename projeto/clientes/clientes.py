class Cliente:
    def __init__(self, nome, morada, telefone, nif, email):
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.nif = nif
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, NIF: {self.nif}, Email: {self.email}"
