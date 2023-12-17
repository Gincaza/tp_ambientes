class Veiculo:
    def __init__(self, marca, modelo, matricula, cor, comprimento, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.cor = cor
        self.comprimento = comprimento
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Veículo: {self.marca} {self.modelo}, Matrícula: {self.matricula}, Cor: {self.cor}"
