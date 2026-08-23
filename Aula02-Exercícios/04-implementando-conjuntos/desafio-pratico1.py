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