from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Restaurante Praça', 'Caseira')
bebida_suco = Bebida('Coca-Cola', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_lasanha = Prato('Lasanha', 2.0, 'A melhor lasanha da cidade')
prato_lasanha.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_lasanha)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main() 