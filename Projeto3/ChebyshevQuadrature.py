import math


class ChebyshevQuadrature:
    
    def chebyQuad(self, f, n):
            
        soma = 0.0
        for i in range(1,n+1):
            soma += (math.pi/n)*(f(math.cos((((2.0*i-1.0)*math.pi)/(2.0*n)))))
        return soma