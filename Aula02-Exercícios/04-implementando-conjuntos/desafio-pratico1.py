""" 
    O Desafio
    Embora o Python possua a estrutura nativa set, seu objetivo aqui é construir uma classe do
    zero que simule o comportamento de um conjunto matemático utilizando apenas listas básicas
    (list).
    Requisitos da Classe MeuConjunto:
    1- O método construtor (__init__) deve receber uma lista de valores e remover qualquer
    elemento duplicado para garantir a propriedade de unicidade.
    2- Implementar um método uniao(outro_conjunto), que retorna um novo objeto do tipo
    MeuConjunto combinando os dados.
    3- Implementar um método intersecao(outro_conjunto), retornando apenas os
    elementos comuns.
"""
class MeuConjunto :
    def __init__ ( self , elementos ) :
        self . dados = []
        for e in elementos :
            if e not in self . dados :
                self . dados . append ( e )

    def uniao ( self , outro ) :
        resultado = self . dados . copy ()
        for e in outro . dados :
            if e not in resultado :
                resultado . append ( e )
        return MeuConjunto ( resultado )

    def intersecao ( self , outro ) :
        resultado = [ e for e in self . dados if e in outro . dados ]
        return MeuConjunto ( resultado )

A = MeuConjunto ([1 , 2 , 2 , 3]) 
B = MeuConjunto ([3 , 4 , 5])

print ( " Uniao : " , A . uniao ( B ) . dados ) 
print ( " Intersecao : " , A . intersecao ( B ) . dados )