class Fatura:
    def __init__(self, cliente, veiculo, data, descricao, valor):
        self.cliente = cliente
        self.veiculo = veiculo
        self.data = data
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"Fatura para: {self.cliente}, Veículo: {self.veiculo}, Data: {self.data}, Valor: {self.valor}"

