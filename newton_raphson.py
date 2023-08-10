
# Blibioteca do python que inclui funções matemáticas
import math

#Definir a função a qual utilizaremos o metodo
def f(x):
    return(x**3-x-1)


#Criar uma função que me dê a derivada da f(x)

def df(x):
    h = 0.0001  
    return((f(x + h) - f(x))/h)

#Criar uma várivavel para o nosso chute inicial (xi); Uma outra variavel para a tolerancia(error); 
error = 0.0001
contador = 0
x = 0.0
xi = 1.5

while(abs(f(xi)) > error):
    
    x = xi - f(xi)/df(xi)
    
    xi = x
    
    contador = contador + 1
    
    if(contador >= 999):
        break


print (f" A raíz é {xi}\n O Numero de iterações: {contador}")