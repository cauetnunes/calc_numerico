# Blibioteca do python que inclui funções matemáticas
import math 

#Definir a função a qual utilizaremos o metodo
def f(x):
	return(x**3 - x - 1.0)

#Definindo a tolerancia

error = 0.000001

# Xn será o a variavel a qual vamos atribuir a raiz da função

xn = 0.0

#Fila que vai representar os indices de x

x = []  

#Intervalo que vamos aplicar o metodo

a = 1
b = 2

#Função para alocar o valor de a na ultima posição da fila

x.append(a)
x.append(b)

contador = 1

#Valor do primeiro indice de xn

n = 1



while(abs(f(xn)) > error):

	xn = x[n] - (x[n] - x[n-1])/(f(x[n]) - f(x[n-1]))*f(x[n])
	x.append(xn)     
	n = n + 1
	contador = contador + 1 

	if(contador >= 9999):
		break 

print (f" A raíz é {xn}\n O Numero de iterações: {contador}")
