from clientes.clientes import Cliente
from veiculos.veiculos import Veiculo
from faturas.faturas import Fatura

# Exemplo de uso:
cliente1 = Cliente("João", "Rua A, 123", "123456789", "123456789", "joao@email.com")
print(cliente1)

veiculo1 = Veiculo("MarcaA", "ModeloX", "ABC123", "Preto", "4 metros", "2000 cc")
print(veiculo1)

fatura1 = Fatura(cliente1, veiculo1, "01/12/2023", "Reparo no motor", 500)
print(fatura1)
