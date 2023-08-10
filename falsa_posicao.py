# Blibioteca do python que inclui funções matemáticas
import math

#Definir duas váriaveis para representarem o intervalo [a,b] e uma váriavel para a tolerancia
a = 1
b = 3
erro = 0.0001
#Definir a função a qual utilizaremos o metodo

def f(x):
    return(x**2-x-2)


#Definir uma váriavel para contar o numero de iterações

contador = 0


xi = (a*f(b) - b*f(a))/(f(b) - f(a))

while(abs(f(xi)) > erro):
    
    if(f(a)*f(xi) < 0.0):
        b = xi
    
    if(f(a)*f(xi) > 0.0):
        a = xi
    
    
    xi = (a*f(b) - b*f(a))/(f(b) - f(a))
    
    
    contador = contador + 1
    
    if(contador > 9999): 
        break

print (f" A raíz é {xi}\n O Numero de iterações: {contador}")