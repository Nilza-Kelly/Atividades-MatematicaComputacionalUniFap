"""
    O Desafio
    Complemente o código anterior, de forma que as operações de união e interseção possam
    receber múltiplos conjuntos como parâmetros.
    Exemplo: A.uniao(B, C), A.uniao(B, C, D, E).
"""
class MeuConjunto :
    def __init__ ( self , elementos ) :
        self . dados = []
        for e in elementos :
            if e not in self . dados :
                self . dados . append ( e )

    def uniao ( self , *outros ) :
        resultado = self . dados . copy ()
        for conjunto in outros:
            for e in conjunto . dados :
                if e not in resultado :
                    resultado . append ( e )
        return MeuConjunto ( resultado )

    def intersecao ( self , *outros ) :
        resultado = self . dados . copy ()
        for conjunto in outros:
            resultado = [e for e in resultado if e in conjunto.dados]
        return MeuConjunto ( resultado )

A = MeuConjunto ([1 , 2 , 2 , 3]) 
B = MeuConjunto ([3 , 4 , 5])
C = MeuConjunto([2, 3, 6])
D = MeuConjunto([3, 6, 7])
E = MeuConjunto([3, 8, 9])

print("União A + B:", A.uniao(B).dados)
print("União A + B + C:", A.uniao(B, C).dados)
print("União A + B + C + D + E:", A.uniao(B, C, D, E).dados)
print("Interseção A + B:", A.intersecao(B).dados)
print("Interseção A + B + C:", A.intersecao(B, C).dados)
print("Interseção A + B + C + D + E:", A.intersecao(B, C, D, E).dados)