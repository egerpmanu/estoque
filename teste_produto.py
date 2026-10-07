from produto import Produto
from produto import Produto

p1 = Produto()
p1.nome = "Playstation"
p1.quantidade = 10
p1.codigo = 67
p1.preco = 4389.00
p1.tipo = " video game"


p2 = Produto()
p2.nome = "GTA IV"
p2.quantidade = 9
p2.codigo = 7
p2.preco = 449.00
p2.tipo = "jogo"

print(f"{p1.nome}: {p1.quantidade} un.")
print(f"{p2.nome}: {p2.quantidade} un.")