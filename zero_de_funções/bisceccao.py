# Blibioteca do python que inclui funções matemáticas

import math

#Definir duas váriaveis para representarem o intervalo [a,b] e uma váriavel para a tolerancia
 
int_a = 1
int_b = 3

error = 0.0001


#Contador para saber o numero de iterações que vão ocorrer no codigo

contador = 0

#Definindo o x0
xi = (int_a + int_b) / 2


#Definir a função a qual utilizaremos o metodo

def f(x):
    return  x**2-x-2                  

#Verificando se no intervalo [a,b] possui raiz. 

if f(int_a)*f(int_b) < 0:
   
    while ((abs(f(int_a) + f(int_b))) / 2 > error):
        
        
        if f(xi) == 0:  
           
            break
          
        else:
            if f(int_a)*f(xi) < 0: 
                int_b = xi
            
            else:
                int_a = xi
           
        contador = contador + 1 
        
        xi = (int_a + int_b)/2        
   
    print (f" A raíz é {xi}\n O Numero de iterações: {contador}")
       

else:
    print("Não existe raiz no intervalo")

